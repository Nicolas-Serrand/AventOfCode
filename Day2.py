from aoc_2022 import *
import collections
import math

DAY = 2

s = get_input(DAY).strip()

def part1():
    score = 0
    for row in s.split("\n"):
        other, me = row.split()
        other = ord(other) - ord('A')
        me = ord(me) - ord('X')
        if other == me:
            outcome_score = 3
        elif (other + 1) % 3 == me:
            outcome_score = 6
        else:
            outcome_score = 0
        shape_score = me + 1
        score += outcome_score + shape_score
    submit(DAY, 1, score)
    
def part2():
    score = 0
    for row in s.split("\n"):
        other, objective = row.split()
        other = ord(other) - ord('A')
        objective = ord(objective) - ord('X')
        if objective == 0:
            me = (other - 1) % 3
        elif objective == 1:
            me = other
        else:
            me = (other + 1) % 3
        outcome_score = objective * 3
        shape_score = me + 1
        score += outcome_score + shape_score
    submit(DAY, 2, score)


if __name__ == "__main__":
    part1() 
    part2()