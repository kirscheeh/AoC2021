#!/usr/bin/env python

import sys
from collections import defaultdict

class Graph(object):

    def __init__(self, connections, directed=False):
        self.graph = defaultdict(set)
        self.directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for start, end in connections:
            self.add(start, end)

    def add(self, start, end):
        self.graph[start].add(end)
        if not self.directed:
            self.graph[end].add(start)
    
    def remove(self, node): # remove references to node
        for n, connection in self.graph.items():
            try:
                connection.remove(node)
            except KeyError:
                pass
        try:
            del self.graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]


    def bfs(self, start, target):
        path = [start]
        vertex_and_path=[start, path]
        bfs_queue = [vertex_and_path]
        visited=set()
        path_all=[]
        
        while bfs_queue:
            current_vertex, path = bfs_queue.pop(0)
            if current_vertex.lower() == current_vertex:
                visited.add(current_vertex)
            
            for neighbour in self.graph[current_vertex]:
                if neighbour == target:
                    path_all.append(path+[neighbour])
                if neighbour not in visited and not neighbour == target:
                    bfs_queue.append([neighbour, path+[neighbour]])
    

    def count_paths(self, small_cave_double, node="start", start="start", target="end", seen=["start"]): #after tip to count directly instead of finding all paths first
        if node == target:
            return 1
        count=0
        for n in self.graph[node]:
            if not n == start:
                if n.isupper() or not n in seen:
                    count += self.count_paths(small_cave_double, n, start, target, seen+[n])
                elif not small_cave_double:
                    count += self.count_paths(True, n, start, target, seen) #dont add small cave to seen here
        return count

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.graph))

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

edges = []

for line in lines:
    first, second = line.split("-")
    edges.append((first, second))


g = Graph(edges)


print("Part 1", g.count_paths(True))

print("Part 2", g.count_paths(False))
