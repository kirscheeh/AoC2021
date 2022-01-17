#!/usr/bin/env python

# Day 8
import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    entries=[]
    for line in lines:
        inp, out = line.split("|")
        inp = inp.split(" ")[:-1] # cause of empty elem
        out = out.split(" ")[1:]
        entries.append((inp, out))
    return entries

def easy_digits(data):
    appearances=0
    for _, signal in data:
        for s in signal:
            if len(s) in [2, 3, 4, 7]:
                appearances+=1
    return appearances

def all_digits(data):

    translator = {frozenset([0, 1, 3, 4, 5, 6]):8, frozenset([0, 1, 2, 4, 5, 6]):0, frozenset([2, 5]):1, frozenset([0, 2, 5]):7, frozenset([0, 2, 3, 4, 6]):2, frozenset([0,1,3,5,6]):5, frozenset([0,2,3,5,6]):3, frozenset([1, 2, 3, 5]):4, frozenset([0,1,3,4,5,6]):6, frozenset([0,1,2,3,5,6]):9}
    
    total=0
    
    for entry, signal in data:
        code={i:[] for i in range(2,8)} #contains numbers based on input
        arrangement={i:"" for i in range(2, 8)} # for making magic and guessing
        
        for e in entry:
            code[len(e)].append(set(e))
        
        arrangement[0] = code[3][0].difference(code[2][0]) #top
        arrangement[2] = code[3][0].intersection(code[2][0]) #upper right
        arrangement[5] = code[3][0].intersection(code[2][0]) #lower right

        arrangement[1] = code[4][0].difference(arrangement[5]) #upper left
        arrangement[3] = code[4][0].difference(arrangement[5]) #middle
        
        # Positions in arangement
        #     0
        # 1       2
        #     3
        # 4       5
        #     6

        sixer=code[6][0] # number with six charcters (0,6,9)
        for elem in code[6]:
            sixer &= elem

        fiver=code[5][0] #five characters (2, 3, 5)
        for elem in code[5]:
            fiver &= elem

        arrangement[1] &= sixer
        arrangement[3] = arrangement[3].difference(arrangement[1])

        sixer = sixer.difference(arrangement[0], arrangement[1])

        fiver.difference(arrangement[0], arrangement[3])

        arrangement[6] = fiver & sixer
        
        arrangement[2] = arrangement[2].difference(sixer)
        arrangement[5] = arrangement[5].difference(arrangement[2])
        
        used="abcdefg" # to get last segment character
        arrangement_helper = {x:0 for x in (list("abcdefg"))}
        for key in arrangement.keys():
            try:
                arrangement_helper[list(arrangement[key])[0]]=key
                used = used.replace(list(arrangement[key])[0], "")
            except IndexError: # happens for last thingy, 4
                continue
        
        arrangement=arrangement_helper
        arrangement[used]=4
        result=[]
        
        for s in signal:
            if len(s) == 2:
                result.append("1")
            elif len(s) == 3:
                result.append("7")
            elif len(s) == 4:
                result.append("4")
            elif len(s) == 7:
                result.append("8")
            else:
                result_set=set()
                
                for s in list(s):
                    result_set.add(arrangement[s])
                
                result.append(str(translator[frozenset(result_set)]))
        
        total += int("".join(result))
    return total
            
data = process_input()

print("Part 1", easy_digits(data))

print("Part 2", all_digits(data))