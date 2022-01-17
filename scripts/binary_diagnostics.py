#!/usr/bin/env python
# Day 3

import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        return f.read().splitlines()

def power_consumption(data):

    digit=[0 for x in range(len(data[0]))]
    
    for binary in data:
        for i in range(len(binary)):
            digit[i]+=int(binary[i])

    gamma=""
    
    for elem in digit:
        if elem > len(data)/2:
            gamma+="1"
        else:
            gamma+="0"
    
    epsilon="".join(["0" if x=="1" else "1" for x in gamma])

    return int(gamma, 2)*int(epsilon, 2)
    
def life_support_rating(data):
    data_oxygen, data_co2 = data, data

    for digit in range(len(data[0])):

        oxygen = sum([int(x[digit]) for x in data_oxygen])
        co2    = sum([int(x[digit]) for x in data_co2])

        if len(data_oxygen) > 1:
            data_oxygen = [x for x in data_oxygen if int(x[digit]) == (oxygen >= len(data_oxygen)/2)]
        
        if len(data_co2) > 1:
            data_co2 = [x for x in data_co2 if int(x[digit]) == (co2 < len(data_co2)/2)]
    
    return int(data_oxygen[0], 2)*int(data_co2[0], 2)
            
            
data = process_input()

print("Part 1", power_consumption(data))
print("Part 2", life_support_rating(data))