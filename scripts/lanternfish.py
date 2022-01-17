#!/usr/bin/env python

# Day 6

import sys

def watch_population(days):
    with open(sys.argv[1], "r") as f:
        lines=f.read().splitlines()
    lines = lines[0].split(",")

    initial_fish = [int(x) for x in lines]
    population=[0]*9
    
    for f in initial_fish:
        population[f]+=1
    
    for day in range(days):
        baby_fish=population[0]
        
        for i in range(len(population)):
            if i == 0:
                continue
            else:
                population[i-1]=population[i]
        
        if not day == 0:
            population[8] =baby_fish
            population[6]+=baby_fish
        
 
    print("\t", sum(population))      
    
print("Part 1", end="\r")
watch_population(80)

print("Part 2", end="\r")
watch_population(256)