#!/usr/bin/env python

# Day 9

import sys
import scipy.ndimage
import numpy as np

def process_input():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    data=[]
    for line in lines:
        data.append(list(map(int, list(line))))
    return data

def risk_levels(data):
    low_points=[]
    for row in range(len(data)):
        for gollum in range(len(data[row])): #checking all corner cases...
            if row == 0:
                if gollum == 0:
                    if data[row][gollum] < data[row+1][gollum] and data[row][gollum] < data[row][gollum+1]:
                        low_points.append(data[row][gollum])
                elif gollum == len(data[row])-1:
                    if data[row][gollum] < data[row][gollum-1] and data[row][gollum] < data[row+1][gollum]:
                        low_points.append(data[row][gollum])
                else:
                    if data[row][gollum] < data[row][gollum-1] and data[row][gollum] < data[row][gollum+1] and data[row][gollum] < data[row+1][gollum]:
                        low_points.append(data[row][gollum])
            elif row == len(data)-1:
                if gollum == 0:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row][gollum+1]:
                        low_points.append(data[row][gollum])
                elif gollum == len(data[row])-1:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row][gollum-1]:
                        low_points.append(data[row][gollum])
                else:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row][gollum+1] and data[row][gollum] < data[row][gollum-1]:
                        low_points.append(data[row][gollum])
            else:
                if gollum == 0:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row+1][gollum] and data[row][gollum] < data[row][gollum+1]:
                        low_points.append(data[row][gollum])
                elif gollum == len(data[row])-1:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row+1][gollum] and data[row][gollum] < data[row][gollum-1]:
                        low_points.append(data[row][gollum])
                else:
                    if data[row][gollum] < data[row-1][gollum] and data[row][gollum] < data[row+1][gollum] and data[row][gollum] < data[row][gollum-1] and data[row][gollum] < data[row][gollum+1]:
                        low_points.append(data[row][gollum])
    return sum([1+x for x in low_points])
    
def largest_basin(data): # after tip to use scipy
    for row in range(len(data)):
        for gollum in range(len(data[row])):
            if data[row][gollum] == 9:
                data[row][gollum] = 0
            else:
                data[row][gollum] = 1
    basins, number  = scipy.ndimage.measurements.label(data)
    basins = basins.tobytes()
    sizes=[]
    for num in range(1, number+1):
        sizes.append(list(basins).count(num))
    return np.prod(sorted(sizes)[-3:])


data = process_input()

print("Part 1", risk_levels(data))

print("Part 2", largest_basin(data))