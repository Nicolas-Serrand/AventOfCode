from aoc_2022 import *
import collections
import math
from functools import cmp_to_key

DAY = 13

inp = get_input(DAY).strip().splitlines()

def compare(first, second):
    if isinstance(first, int) and isinstance(second, int):
        if first == second:
            return 0
        else:
            return -1 if first < second else 1
    if isinstance(first, list) and isinstance(second, list):
        for a, b in zip(first, second):
            if compare(a, b) != 0:
                return compare(a, b)
        if len(first) == len(second):
            return 0
        return -1 if len(first) < len(second) else 1
    elif isinstance(first, int):
        return compare([first], second)
    elif isinstance(second, int):
        return compare(first, [second])
    else:
        raise ValueError(first, second)
            
        
def part1():
    i = 1
    ans = 0
    for first, second in zip(inp, inp[1:]):
        if first and second:
            first = eval(first)
            second = eval(second)
            if compare(first, second) < 0:
                ans += i
            i += 1
    submit(DAY, 1, ans)
            
          
def part2():
    packets = [[[2]], [[6]]]
    for first, second in zip(inp, inp[1:]):
        if first and second:
            packets.append(eval(first))
            packets.append(eval(second))
    packets.sort(key=cmp_to_key(compare))
    ans = (1 + packets.index([[2]])) * (1 + packets.index([[6]]))
    submit(DAY, 2, ans)                    
      
      
if __name__ == "__main__":
    part1() 
    part2()