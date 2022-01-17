#!/usr/bin/env python

# Day 14

import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    template=lines[0]
    rules = {}
    for line in lines[2:]:
        x, y = line.split(" -> ")
        rules[x]=y

    return template, rules

def polymerization(template, rules, steps):
    for step in range(steps):
        working_template=template[0]
        for i in range(0, len(template)-1):
            if template[i:i+2] in rules.keys():
                working_template += rules[template[i:i+2]]+template[i+1]
        template = working_template
    return template

def polymerization_complex(template, rules, steps):
    elements = {i:template.count(i) for i in set(template)}
    template_1 = {template[i:i+2]:0 for i in range(len(template)-1)}
    
    for i in range(len(template)-1):
        template_1[template[i:i+2]]+=1
    template = template_1

    for step in range(steps):
        working={}
        for key in template.keys():
            if key in rules.keys():
                try:
                    working[key[0]+rules[key]]+=template[key]
                except KeyError:
                    working[key[0]+rules[key]]=template[key]
                try:
                    working[rules[key]+key[1]]+=template[key]
                except KeyError:
                    working[rules[key]+key[1]]=template[key]
                try:
                    elements[rules[key]]+=template[key]
                except KeyError:
                    elements[rules[key]]=template[key]               
            else:
                try:
                    working[key]+=template[key]
                except KeyError:
                    working[key]=template[key]
        template=working.copy()
    return template, elements

template, rules = process_input()

polymer = polymerization(template, rules, 10)

most = max(polymer.count(x) for x in set(polymer))
least = min(polymer.count(x) for x in set(polymer))
print("Part 1", most-least)

polymers, elements = polymerization_complex(template, rules, 40)

most = max(elements.values())
least=min(elements.values())
print("Part 2", most-least)

