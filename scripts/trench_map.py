#!/usr/bin/env python

import sys 

def process_input(max_size):
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()

    enhancement_algo=list(lines[0])
    picture=[]
    half_size=int(max_size/2)
    
    for i in range(max_size):
        picture.append(["."]*(len(lines[3])+max_size))
    for line in lines[2:]:
        picture.append(["."]*half_size+list(line)+["."]*half_size)#  ["."]*10
    for i in range(max_size):
        picture.append(["."]*(len(lines[3])+max_size))
    return enhancement_algo, picture

def convert_image(picture, algo, steps):
    output = [list("0"*(len(picture[0]))) for i in range(len(picture))]
    for row in range(len(picture)):
        for gollum in range(len(picture[row])):
            neighbours = [(row-1, gollum-1), (row-1, gollum), (row-1, gollum+1), (row, gollum-1), (row, gollum), (row, gollum+1), (row+1, gollum-1), (row+1, gollum), (row+1, gollum+1)]
            binary=""
            for x, y in neighbours:
                if 0 <= x < len(picture) and 0 <= y < len(picture[row]):
                    binary += str(int(picture[x][y]=="#"))
                else:
                    if steps%2 == 0:
                        binary += "1"
                    else:
                        binary+="0"
            
            index = int(binary, 2)
            output[row][gollum] = algo[index]


    return output

def count_light(picture):
    data = []
    for line in picture:
        data.extend(line)
    return data.count("#")

iterations=50

enhancement_algo, picture = process_input(iterations*2)
for steps in range(iterations):
    picture = convert_image(picture, enhancement_algo, steps+1)
    if steps == 1:
        print("Part 1", count_light(picture))

print("Part 2", count_light(picture))