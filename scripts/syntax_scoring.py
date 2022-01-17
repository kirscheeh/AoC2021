#!/usr/bin/env python

# Day 10

import sys

def process_input():
    with open(sys.argv[1], "r") as f:
        return f.read().splitlines()


def syntax_error_scores(data):
    dict_translate={"(":")", "[":"]", "{":"}", "<":">"}
    dict_prices={")":3, "]":57, "}":1197, ">":25137}
    
    errorneous_brackets=[]
    for line in data:
        helper_brackets=""
        for bracket in line:
            if bracket in dict_translate.keys():
                helper_brackets = dict_translate[bracket]+helper_brackets
            else:
                if bracket == helper_brackets[0]:
                    helper_brackets = helper_brackets[1:]
                else:
                    errorneous_brackets.append(bracket)
                    break
    return sum([dict_prices[x] for x in errorneous_brackets])

def autocomplete(data):
    
    dict_translate={"(":")", "[":"]", "{":"}", "<":">"}
    dict_prices={")":1, "]":2, "}":3, ">":4}
    
    total_score=0
    scoring=[]
    
    for line in data:
        helper_brackets=""
        for bracket in line:
            if bracket in dict_translate.keys():
                helper_brackets = dict_translate[bracket]+helper_brackets
            else:
                if bracket == helper_brackets[0]:
                    helper_brackets = helper_brackets[1:]
                else:
                    break # then this line is incorrect, ignore here
        else:
            total_score=0
            for b in helper_brackets:
                total_score*=5
                total_score+=dict_prices[b]
            scoring.append(total_score)

    return sorted(scoring)[int(len(scoring)/2)]


data = process_input()

print("Part 1", syntax_error_scores(data))

print("Part 2", autocomplete(data))
