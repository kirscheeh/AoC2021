#!/usr/bin/env python

# Day 13

import sys
from tkinter import *

def process_input():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    dots=set()
    instructions=[]
    for line in lines:
        if "fold along" in line:
            line = line.split("=")
            axis = line[0][-1]
            coord = int(line[1])
            instructions.append((axis=="x", coord))
        elif "," in line:
            line = line.split(",")
            dots.add((int(line[0]), int(line[1])))
        else:
            continue
    return dots, instructions

def folding(dots, instructions):
    for i, (axis, coord) in enumerate(instructions):
        if i == 1:
            print("Part 1", len(dots))
        to_remove=set()
        to_add=set()
        if axis: # x
            for x, y, in dots:
                if x > coord:
                    to_remove.add((x,y))
                    to_add.add((coord-(x-coord), y))
        else: #y
            for x, y, in dots:
                if y > coord:
                    to_remove.add((x,y))
                    to_add.add((x, coord-(y-coord)))

        dots -= to_remove
        dots.update(to_add)
    return dots

def visualize_code(p_dots):
    max_x = max([x[0] for x in p_dots])
    max_y = max([x[1] for x in p_dots])
    root = Tk()
    frame = Frame(root)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="news")
    grid = Frame(frame)
    grid.grid(sticky="news", column=0, row=7, columnspan=2)
    frame.rowconfigure(7, weight=1)
    frame.columnconfigure(0, weight=1)
    #example values
    for x in range(max_x+1):
        for y in range(max_y+1):
            if (x, y) in p_dots:
                color="green"
            else:
                color="gray"
            btn = Button(frame, bg=color)
            btn.grid(column=x, row=y, sticky="news")

    frame.columnconfigure(tuple(range(max_x)), weight=1)
    frame.rowconfigure(tuple(range(max_y)), weight=1)

    root.mainloop()

dots, instructions = process_input()

number = folding(dots, instructions)

# Part 2
visualize_code(number)