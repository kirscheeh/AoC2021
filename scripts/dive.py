#!/usr/bin/env python
# Day 2

import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        data = f.read().splitlines()
    
    commands = []

    for line in data:
        direction, steps = line.split(" ")
        
        if direction == "forward":
            direction = 1
        else:
            if direction == "up":
                steps=int(steps)*-1
            
            direction=0
        
        commands.append((direction, int(steps)))

    return commands

def simple_piloting(data):
    x, y = 0, 0

    for direction, steps in data:
        if direction:
            x+=steps
        else:
            y+=steps

    return x*y

def piloting_with_aim(data):
    x, y, aim = 0, 0, 0

    for direction, steps in data:
        if direction:
            y+=aim*steps
            x+=steps
        else:
            aim+=steps
    
    return x*y


data = process_input()

print("Part 1", simple_piloting(data))

print("Part 2", piloting_with_aim(data))
    