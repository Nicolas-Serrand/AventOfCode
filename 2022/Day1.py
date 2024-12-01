from aoc_2022 import *
import collections
import math
#import networkx as nx

DAY = 1

s = get_input(DAY).strip()

def part1():
    elves = []
    for k in s.split("\n\n"):
        elves.append(sum(ints(k)))
    ans = max(elves)
    print(ans)
    submit(DAY, 1, ans)
    
def part2():
    elves = []
    for k in s.split("\n\n"):
        elves.append(sum(ints(k)))
    top = []
    for _ in range(3):
        top.append(max(elves))
        elves.remove(top[-1])
    ans = sum(top)
    submit(DAY, 2, ans)

if __name__ == "__main__":
    part1() 
    part2()