#!/usr/bin/env python

import sys
import math

def process_positions():
    return list(map(int, open(sys.argv[1], "r").read().split(",")))

def align_crabs_linear(data):
    positions = {x:0 for x in set(data)}
    
    for pos in positions:
        positions[pos] = sum([abs(x-pos) for x in data])

    return min(positions.values())

def align_crabs_exponential(data):
    positions = {x:0 for x in range(max(data)+1)}
    
    for pos in positions:
        positions[pos] = sum([sum([i for i in range(abs(x-pos)+1)]) for x in data])

    return min(positions.values())

data = process_positions()

print("Part 1", align_crabs_linear(data))
print("Part 2", align_crabs_exponential(data)) #slow

