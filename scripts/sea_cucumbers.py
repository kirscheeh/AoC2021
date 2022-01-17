#!/usr/bin/env python

import sys

def printer(data):
    d = [["0"]*num_cols for i in range(num_rows)]
    for x, y in data[">"]:
        d[x][y]=">"
    for x, y in data["v"]:
        d[x][y]="v"

    for h in d:
        print(h)

data={">":set(), "v":set(), ".":set()}

f = open(sys.argv[1], "r").read().splitlines()

num_rows=len(f)
num_cols = len(f[0])

for i, line in enumerate(f):
    for j, c in enumerate(line):
        data[c].add((i, j))

counter=0

while True:
    counter+=1
    
    moved=0
    
    east=set()
    
    for x, y in data[">"]:
        pair=(x, y+1)
        
        if y+1 >= num_cols:
            pair=(x, 0)
        
        if pair not in data[">"] and pair not in data["v"]:
            east.add(pair)
            moved+=1
        else:
            east.add((x, y))
    
    data[">"] = east

    south=set()

    for x, y in data["v"]:
        pair=(x+1, y)
        
        if x+1 >= num_rows:
            pair=(0, y)
        
        if pair not in data[">"] and pair not in data["v"]:
            south.add(pair)
            moved+=1
        else:
            south.add((x, y))

    if moved == 0:
        break
    
    data["v"] = south
     
print("Part 1", counter)
