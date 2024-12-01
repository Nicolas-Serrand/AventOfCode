from aoc_2022 import *
import collections
import math

DAY = 10

inp = get_input(DAY).strip().splitlines()
#inp = get_example(DAY, 1).splitlines()

def part1():
    queue = collections.deque()
    x = 1
    i = 0
    ans = 0
    for row in inp:  
        if row == "noop":
            queue.append(0)
        elif row.startswith("addx"):
            v = int(row.split()[1])
            queue.extend([0, v])
        while queue:
            i += 1
            if (i - 20) % 40 == 0:
                print(i * x)
                ans += i * x
            x += queue.popleft()
    submit(DAY, 1, ans)
        

    
def part2():
    queue = collections.deque()
    x = 1
    i = 0
    ans = ""
    for row in inp:  
        if row == "noop":
            queue.append(0)
        elif row.startswith("addx"):
            v = int(row.split()[1])
            queue.extend([0, v])
        while queue:
            if abs(i - x) < 2:
                ans += '#'
            else:
                ans += '.'
            x += queue.popleft()
            i += 1
            if i % 40 == 0:
                ans += "\n"
                i = 0
    print(ans)
    # Submit the answer prompted (for me ERCREPCJ)
    
if __name__ == "__main__":
    part1() 
    part2()