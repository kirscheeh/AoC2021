#!/usr/bin/env python
#Day 4

import sys

def get_numbers(lines):
    return [int(x) for x in lines[0].split(",")]

def generate_boards(lines):
    index=2
    boards={}
    counter=0
    
    while index < len(lines):
        boards[counter]=[]
        numbers=[]
        for i in range(5):
            row = [int(x.replace("\n", "")) for x in lines[index+i].split(" ") if not x == ""]
            numbers+=row
        boards[counter]=numbers
        counter+=1
        index+=6
        
    return boards

def check_row(numbers):
    for i in range(0, len(numbers), 5):
        result="".join([str(x) for x in numbers[i:i+5]])
        if result == "":
            return True
    return False

def check_column(numbers):
    for i in range(0, 5):
        result=""
        for j in range(0,25, 5):
            result+=str(numbers[i+j])
        if result == "":
            return True
    return False

def check_diagonal(numbers):
    result=""

    for i in range(0, 30, 6):
        result+=str(numbers[i])
    
    if result=="":
        return True
    else:
        return False

def winning():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    
    number = get_numbers(lines)
    
    boards = generate_boards(lines)
    
    for num in number:
        for key in boards.keys():
            if num in boards[key]:
                boards[key] = ["" if x == num else x for x in boards[key]]
            if check_row(boards[key]) or check_column(boards[key]) or check_diagonal(boards[key]):
                return boards[key], num

def losing():
    
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()
    
    number = get_numbers(lines)
    boards = generate_boards(lines)
    copied_boards=boards.copy()
    
    for num in number:
        for key in boards.keys():
            if key in copied_boards.keys():
                if num in boards[key]:
                    boards[key] = ["" if x == num else x for x in boards[key]]
                if check_row(boards[key]) or check_column(boards[key]) or check_diagonal(boards[key]):
                    if len(copied_boards.keys()) == 1:
                        return boards[key], num 
                    del copied_boards[key]

def calculate_number(numbers, num):
    result=0
    for elem in numbers:
        if not elem=="":
            result+=int(elem)
    print(result*num)

board, num = winning()

calculate_number(board, num)

board, num = losing()

calculate_number(board, num)