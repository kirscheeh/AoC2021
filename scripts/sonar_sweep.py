#!/usr/bin/env python
# Day 1

import sys

def process_input(file):
    with open(file, "r") as depths:
        data = depths.readlines()
    depths = [int(x[:-1]) for x in data]
    return depths

def count_increases_simple(depths):
    counter=0
    for i in range(len(depths)):
        if i == 0:
            continue
        else:
            if depths[i-1] < depths[i]:
                counter+=1
    return counter

def count_increased_window(depths):
    counter=0

    current_frame = depths[0]+depths[1]+depths[2]
    
    for i in range(len(depths)):
        if i < len(depths)-3:

            next_frame = depths[i+1]+depths[i+2]+depths[i+3]

            if current_frame < next_frame:
                counter+=1

            current_frame = next_frame
        else:
            continue
    return counter

depths = process_input(sys.argv[1])

print("Task 1:", count_increases_simple(depths))
print("Task 2:", count_increased_window(depths))