#!/usr/bin/env python
# Day 17

import sys

# "target area: x=70..125, y=-159..-121"

height = (70, 125)
width = (-159, -121)

probe_x, probe_y = 0, 0
velocity_start_x, velocity_start_y = 0, 0
velocity_x, velocity_y = velocity_start_x, velocity_start_y

def find_x(start, end):
    velocity_x = []
    for i in range(1, end+1):
        probe=0
        velocity=i
        target_area=False
        while not target_area:
            probe+=velocity
            
            if velocity > 0:
                velocity -= 1
            elif velocity < 0:
                velocity+=1
            else:
                if not start <= probe <= end:
                    break
            
            if probe > end:
                break
            
            if start <= probe <= end:
                target_area=True
                break
        if target_area:
            velocity_x.append(i)
    return velocity_x

def find_y(xvals, start_y, end_y, start_x, end_x):
    velocities=[]
    for velx in xvals:
        for i in range(start_y, abs(start_y)):
            probe_x, probe_y=0,0
            velocity_y = i
            velocity_x = velx
            target_area = False
            while not target_area:
                
                probe_x += velocity_x
                probe_y += velocity_y
                
                if velocity_x > 0:
                    velocity_x -= 1
                elif velocity_x < 0:
                    velocity_x+=1
                else:
                    if not start_x <= probe_x <= end_x:
                        break
                
                velocity_y-=1
                if start_x <= probe_x <= end_x and start_y <= probe_y <= end_y:
                    target_area=True
                    break

                if probe_y < start_y:
                    break

                if probe_x > end_x:
                    break

            if target_area:
                velocities.append((velx, i))
    return velocities

def find_height(vectors, height, width):
    start_x, end_x = height
    start_y, end_y = width
    max_height=0
    
    for vel_x, vel_y in vectors:
        probe_x, probe_y = 0,0
        velocity_x = vel_x
        velocity_y = vel_y
        while True:    
            probe_x += velocity_x
            probe_y += velocity_y    
            
            if velocity_x > 0:
                velocity_x -= 1
            elif velocity_x < 0:
                velocity_x+=1
            else:
                if not start_x <= probe_x <= end_x:
                    break
                
            velocity_y-=1

            if probe_y < start_y:
                break

            if probe_x > end_x:
                break

            if probe_y >= max_height:
                max_height=probe_y
    return max_height

xvals = find_x(height[0], height[1])

vectors = find_y(xvals, width[0], width[1], height[0], height[1])

max_y = find_height(vectors, height, width)

print("Part 1", max_y)
print("Part 2", len(vectors))
