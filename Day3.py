from aoc_2022 import *
import collections
import math

DAY = 3

inp = get_input(DAY).strip().split("\n")
#inp = get_example(DAY).strip().split("\n")

def part1():
    ans = 0
    for i, row in enumerate(inp):
        compartment_1 = row[:len(row)//2]
        compartment_2 = row[len(row)//2:]    
        for c in compartment_1:
            if c in compartment_2:
                if c.isupper():
                    ans += ord(c) - ord('A') + 27
                elif c.islower():
                    ans += ord(c) - ord('a') + 1
                break
    submit(DAY, 1, ans)
                        
    
def part2():
    ans = 0
    for i in range(0, len(inp), 3):
        rucksack_1, rucksack_2, rucksack_3 = set(inp[i]), set(inp[i+1]), set(inp[i+2])
        badge = rucksack_1.intersection(rucksack_2).intersection(rucksack_3).pop()
        if badge.isupper():
            ans += ord(badge) - ord('A') + 27
        elif badge.islower():
            ans += ord(badge) - ord('a') + 1
    submit(DAY, 2, ans)
                

if __name__ == "__main__":
    part1() 
    part2()