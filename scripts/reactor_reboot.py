#!/usr/bin/env python
# Day 22
import sys

def part1():

    on=set()
    for line in open(sys.argv[1], "r").read().splitlines():
        name, coordinates = line = line.split(" ")
        coordinates = coordinates.split(",")
        ranges=[]
        
        for coord in coordinates:
            first, end  = coord.split("..")
            _, start = first.split("=")
            
            if -50 <= int(start) <= 50 and -50 <= int(end) <= 50:
                ranges.append((int(start), int(end)))

        if len(ranges) == 3: 
            coords = set([(x,y,z) for x in range(ranges[0][0], ranges[0][1]+1) for y in range(ranges[1][0], ranges[1][1]+1) for z in range(ranges[2][0], ranges[2][1]+1)])
            if name == "on":
                on.update(coords)
            else:
                on.difference_update(coords)

    print("Part 1", len(on))

def part2(): # DOES NOT WORK
    on=set()
    for line in open(sys.argv[1], "r").read().splitlines():
        name, coordinates = line = line.split(" ")
        coordinates = coordinates.split(",")
        ranges=[]
        
        for coord in coordinates:
            first, end  = coord.split("..")
            _, start = first.split("=")
            
            ranges.append((int(start), int(end)))

        if len(ranges) == 3: # here i need to make big cubes and then check for intersections
            coords = set([(x,y,z) for x in range(ranges[0][0], ranges[0][1]+1) for y in range(ranges[1][0], ranges[1][1]+1) for z in range(ranges[2][0], ranges[2][1]+1)])
            if name == "on":
                on.update(coords)
            else:
                on.difference_update(coords)

    print(len(on))

part1()
    