from aoc_2022 import *
import collections
import math

DAY = 6

inp = get_input(DAY).strip()

def part1():
    offset = 4
    for i in range(len(inp) - offset):
        chars = inp[i:i + offset]
        if all(chars.count(c) == 1 for c in chars):
            ans = i + offset
            submit(DAY, 1, ans)
            return
    raise Exception("Error: marker not found.")

def part2():
    offset = 14
    for i in range(len(inp) - offset):
        chars = inp[i:i + offset]
        if all(chars.count(c) == 1 for c in chars):
            ans = i + offset
            submit(DAY, 2, ans)
            return
    raise Exception("Error: marker not found.")

    
if __name__ == "__main__":
    part1() 
    part2()