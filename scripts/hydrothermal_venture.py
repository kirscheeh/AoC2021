#!/usr/bin/env python
# Day 5

import sys

def counting_vents(diagonal=False):
    lines = open(sys.argv[1], "r").readlines()
    
    length_x, length_y = 0, 0
    
    pipes=[]
    
    for line in lines:
        start, end = line.split("->")
        
        start_x, start_y, end_x, end_y = [int(x.rstrip()) for x in start.split(",")]+[int(x.rstrip()) for x in end.split(",")]

        length_x = max(length_x, start_x, end_x)
        
        length_y = max(length_y, start_y, end_y)

        pipes.append([start_x, start_y, end_x, end_y])

    data = [[0 for x in range(length_x+1)] for y in range(length_y+1)]
    vents=0
    
    for pipe in pipes:
        if pipe[0] == pipe[2]: #same x
            for i in range(min(pipe[1], pipe[3]), max(pipe[1], pipe[3])+1):
                data[i][pipe[0]]+=1
                if data[i][pipe[0]] == 2:
                    vents+=1
                
        elif pipe[1] == pipe[3]: #same x
            for i in range(min(pipe[0], pipe[2]), max(pipe[0], pipe[2])+1):
                data[pipe[1]][i]+=1
                if data[pipe[1]][i] == 2:
                    vents+=1
        else: 
            if diagonal: #diagonal

                steps_x, steps_y=1, 1

                if pipe[0] > pipe[2] and pipe[1] > pipe[3]: # pipe is inversed
                    pipe[0], pipe[2] = pipe[2], pipe[0]+1
                    pipe[1], pipe[3] = pipe[3], pipe[1]+1
   
                elif pipe[1] > pipe[3]: # start higher than end
                    steps_y=-1
                    pipe[2]+=1
                    pipe[3]-=1
                
                elif pipe[0] > pipe[2]: # start more right than end
                    steps_x=-1
                    pipe[2]-=1
                    pipe[3]+=1
                
                else: # start is lower and more left than end
                    pipe[2]+=1
                    pipe[3]+=1
                
                for i, j in zip(range(pipe[0], pipe[2], steps_x), range(pipe[1], pipe[3], steps_y)):
                    data[j][i]+=1
                    if data[j][i] == 2:
                        vents+=1
            else:
                continue
        
    return vents

print("Part 1", counting_vents(0))
print("Part 2", counting_vents(1))