#!/usr/bin/env python

import sys
from functools import lru_cache

# Day 21

def awesome_dice(score, start_1, start_2):
    dice = [x%100 if x != 100 else 100 for x in range(1, 200)]
    score_player_1=0
    score_player_2=0
    position_dice=0
    rounds=1

    while score_player_1 < score and score_player_2 < score:
        
        if (rounds-1) % 2 == 0: # player 1
            start_1 += sum(dice[position_dice:position_dice+3])
            start_1 %= 10
            score_player_1+=(start_1+1)
        else: #player 2
            start_2 += sum(dice[position_dice:position_dice+3])
            start_2 %= 10
            score_player_2+=(start_2+1)
            
        rounds+=1
        position_dice+=3
        position_dice%=100

    return (rounds*3-3)*min(score_player_2, score_player_1)

def new_position(pos, step):
    return (pos+step-1) % 10 +1

@lru_cache(maxsize=None)
def multiverse(start_1, start_2, score_1, score_2, score_max, num_rolls, turn_p1):
    if score_1 >= score_max:
        return 1
    if score_2 >= score_max:
        return 0

    wins=0

    if turn_p1:
        if num_rolls > 0:
            for roll in range(1, 4):
                wins += multiverse(new_position(start_1, roll), start_2, score_1, score_2, score_max, num_rolls-1, True) 
        else:
            wins += multiverse(start_1, start_2, score_1+start_1, score_2, score_max, 3, False) # now player two

    else:
        if num_rolls > 0:
            for roll in range(1, 4):
                wins += multiverse(start_1, new_position(start_2, roll), score_1, score_2, score_max, num_rolls-1, False) 
        else:
            wins += multiverse(start_1, start_2, score_1, score_2+start_2, score_max, 3, True) # now player one

    return wins

def who_won_most(start_1, start_2):
    return max(multiverse(start_1, start_2, 0, 0, 21, 3, True), multiverse(start_1, start_2, 0, 0, 21, 3, False))

start_player_1_e=3 # 0-based
start_player_2_e=7 # 0-based
score_1 = 1000
score_2 = 21
print("Part 1", awesome_dice(score_1, start_player_1_e, start_player_2_e))

start_1b_1=1
start_1b_2=10

print("Part 2", who_won_most(start_1b_1, start_1b_2)) # tip for using lru_cache