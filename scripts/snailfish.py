#!/usr/bin/env python

import sys 
import json
from collections.abc import Iterable
import re

def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def add(l1: list, l2: list) -> str:
    return f"[{l1}, {l2}]"

def explode(l):
    num_brackets=0
    linear_number = list(flatten(json.loads(l)))
    for i, c in enumerate(l):
        if c == "[":
            num_brackets+=1
        elif c == "]":
            num_brackets-=1
        
        if num_brackets == 5:
            break
    else:
        return l
    
    index_number = re.search("\[\d{1,},\d{1,}\]", l[i:])
    index_pair_left = len(re.findall("\d+", l[:i+1]))
    index_pair_right= index_pair_left+1
    pair = json.loads(index_number.group())
    
    left = index_pair_left-1
    right = index_pair_right+1
    try:
        linear_number[left]+=pair[0]
        new_left=re.sub("(\d+)(?!.*\d)" , str(linear_number[left]), l[:i+index_number.start()]) 
    except IndexError:
        new_left=l[:i+index_number.start()]
    try: 
        linear_number[right]+=pair[1]
        new_right=re.sub("\d+", str(linear_number[right]), l[i+index_number.start()+len(index_number.group()):], count=1) 
    except IndexError:
        new_right=l[i+index_number.start()+len(index_number.group()):]

    l = new_left + "0"+ new_right 
    return l

def split(l):
    for i, num in enumerate(flatten(json.loads(l))):
        if num > 9:
            if num % 2 == 0:
                val1, val2 = int(num/2), int(num/2)
            else:
                val1 = int(num/2)
                val2 = val1+1
            pair_to_add = f"[{val1},{val2}]"
            break
    else:
        return l
    
    index_number = re.search("[1-9]{1}[0-9]", l)
    l = l[:index_number.start()]+pair_to_add+l[index_number.start()+len(index_number.group()):]
    return l
        
def reduce(l):
    unchanged=0
    while True:
        num_brackets=0
        for index, c in enumerate(l):
            if c == "[":
                num_brackets+=1
                if num_brackets == 5:
                    l = explode(l)
                    unchanged=0
                    break
            elif c == "]":
                num_brackets-=1

            if num_brackets == 5:
                l = explode(l)
                unchanged=0
                break
        else:
            unchanged+=1
        if unchanged < 1:
            continue
        
        linear_number = list(flatten(json.loads(l)))
        if max(linear_number) > 9:
            l = split(l)
            unchanged=0
        else:
            unchanged+=1
        if unchanged > 2:
            return l

def onestep(l1, l2):
    number = add(l1, l2)
    number = reduce(number)
    number = number.replace(" ", "")
    return number

def magnitude(l):
    matches = re.findall("\[\d+,\d+\]", l)
    while matches: 
        for m in matches:
            left, right = json.loads(m)

            l =l.replace(m, str(3*left+2*right))
        matches = re.findall("\[\d+,\d+\]", l)
    return int(l)

numbers = [x.replace(" ", "") for x in open(sys.argv[1], "r").read().splitlines()]

# Part 1
number = numbers[0]
for num in numbers[1:]:
    number = onestep(number, num)

print("Part 1", magnitude(number))


# Part 2
magnitudes=[]

for one in numbers:
    for two in numbers:
        number = onestep(one, two)
        magnitudes.append(magnitude(number))
        
        number = onestep(two, one)
        magnitudes.append(magnitude(number))

print("Part 2", max(magnitudes)) # slow

