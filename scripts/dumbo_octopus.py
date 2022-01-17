#!/usr/bin/env python

# Day 11

import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    
    d=[]
    
    for row in lines:
        d.append(list(map(int, list(row))))
    
    neighbours={(i, j):[] for i in range(len(d)) for j in range(len(d[i]))}
    
    for i in range(len(d)):
        for j in range(len(d[i])):
            n = [(i-1, j), (i-1, j-1), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j), (i+1, j-1), (i+1, j+1)]
            result=[]
            for elem in n:
                if elem[0] >= 0 and elem[1] >= 0 and elem[0] <= 9 and elem[1] <= 9:
                    result.append(elem)
            neighbours[(i, j)] = result
    return d, neighbours

def recharge(octo, neighbours, row, gollum):
    flashes=0
    for x, y in neighbours[(row, gollum)]:
        
        if octo[x][y] == 9:
            continue
        elif octo[x][y] == -1:
            continue
        else:
            octo[x][y]+=1
            if octo[x][y] == 9:
                flashes += 1
                flashes += recharge(octo, neighbours, x, y)
                octo[x][y]=-1
    return flashes

def count_flashes(octo, neighbours, steps):
    flashes=0
    for i in range(steps):
        for row in range(len(octo)):
            for gollum in range(len(octo[row])):
                if octo[row][gollum] == 9:
                    flashes+=1
                    flashes+=recharge(octo, neighbours, row, gollum)
                    octo[row][gollum]=-1
        for row in range(len(octo)):
            for gollum in range(len(octo[row])):
                octo[row][gollum]+=1

    return flashes
            
def simoultanous_flash(grid, neighbours):
    steps=0
    flash=False
    flashes=0
    while not flash:
        for row in range(len(grid)):
            for gollum in range(len(grid[row])):
                if grid[row][gollum] == 9:
                    flashes+=1
                    flashes+=recharge(grid, neighbours, row, gollum)
                    grid[row][gollum]=-1
        zeros=0
        for row in range(len(grid)):
            for gollum in range(len(grid[row])):
                grid[row][gollum]+=1
                if grid[row][gollum]==0:
                    zeros+=1
        if zeros == 100:
            flash=True
        else:
            steps+=1
    return steps+1


data, neighbours = process_input()

flashes = count_flashes(data, neighbours, 100)

print("Part 1", flashes)

#data, neighbours = process_input()

print("Part 2", simoultanous_flash(data, neighbours)+100) # not sure why i need to add the previous 100

