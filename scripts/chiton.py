#!/usr/bin/env python

import sys
from queue import PriorityQueue
from functools import lru_cache

def process_input() -> list:
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()

    data = []
    data_oneline=[]
    for d in lines:
        data.append(list(map(int, d)))
        data_oneline.extend(list(map(int, d)))

    neighbours = {}
    count=0
    for row in range(len(data)):
        for gollum in range(len(data[row])):
            poss_neigh = [(row-1, gollum),(row+1, gollum ),(row, gollum-1),(row, gollum+1)]
            #neighbours[(row, gollum)] = []
            neighbours[count] = []
            for x, y in poss_neigh:
                n=count
                if 0 <= x < len(data) and 0 <= y < len(data[row]):
                    #neighbours[(row, gollum)].append((x, y))
                    if x == row-1:
                        n-=len(data[row])
                    elif x == row+1:
                        n+=len(data[row])
                    if y == gollum-1:
                        n-=1
                    elif y == gollum+1:
                        n+=1
                    neighbours[count].append(n)
            count+=1

    return data_oneline, neighbours

data, neighbours = process_input()

class Graph:
    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        #self.edges[v][u] = weight

@lru_cache(maxsize=None)
def dijkstra(graph, start, stop=None):
    D = {v:float('inf') for v in range(graph.v)}
    D[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, current) = pq.get()
        graph.visited.append(current)

        if current == stop:
            return D

        for neighbour in range(graph.v):
            if graph.edges[current][neighbour] != -1:
                distance = graph.edges[current][neighbour]
                if neighbour not in graph.visited:
                    old = D[neighbour]
                    new = D[current] + distance
                    if new < old:
                        pq.put((new, neighbour))
                        D[neighbour] = new
    return D

"""g = Graph(len(neighbours))

for key in neighbours.keys():
    for neighbour in neighbours[key]:
        g.add_edge(key, neighbour, data[neighbour])

D = dijkstra(g, 0, 9999)

# Part 1
print(D[9999])"""
@lru_cache(maxsize=None)
def create_big_map():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()

    data_b = []
    for row in lines:
        o = list(map(int, row))
        e = o

        for i in range(4):
            e = [x+1 if x <= 8 else 1 for x in e]
            o.extend(e)
        
        data_b.append(o)
    
    data_w = data_b.copy()
    counter = 0

    for i in range(1, 5):
        for d in data_b:
            e = [x+1 if x <= 8 else 1 for x in d]
            data_w.append(e)
        data_b = data_w[i*10:i*10+10]

    data = data_w

    data_oneline=[]
    for d in data_w:
        data_oneline.extend(d)

    neighbours = {}
    count=0
    for row in range(len(data)):
        for gollum in range(len(data[row])):
            poss_neigh = [(row-1, gollum),(row+1, gollum ),(row, gollum-1),(row, gollum+1)]
            neighbours[count] = []
            for x, y in poss_neigh:
                n=count
                if 0 <= x < len(data) and 0 <= y < len(data[row]):
                    if x == row-1:
                        n-=len(data[row])
                    elif x == row+1:
                        n+=len(data[row])
                    if y == gollum-1:
                        n-=1
                    elif y == gollum+1:
                        n+=1
                    neighbours[count].append(n)
            count+=1

    return data_oneline, neighbours
        


# technically it works, practically kills the laptop
"""data, neighbours = create_big_map()

g = Graph(len(neighbours))

for key in neighbours.keys():
    for neighbour in neighbours[key]:
        g.add_edge(key, neighbour, data[neighbour])

D = dijkstra(g, 0, len(neighbours)-1)

print(D[len(neighbours)-1])"""

