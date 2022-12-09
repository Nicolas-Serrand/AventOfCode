from aoc_2022 import *
import collections
import math

DAY = 9

inp = get_input(DAY).strip().splitlines()
#inp = get_example(DAY, 3).splitlines()

directions = {'R':(0, 1), 'L':(0, -1), 'U':(1, 0), 'D':(-1, 0)}

def move_tail(head, tail):
    diff = (head[0] - tail[0], head[1] - tail[1])
    if abs(diff[0]) <= 1 and abs(diff[1]) <= 1:
        return tail
    tail_x, tail_y = tail
    if 1 < abs(diff[0]):
        tail_x += 1 if 0 < diff[0] else -1
        if 0 < abs(diff[1]):
            tail_y += 1 if 0 < diff[1] else -1
    elif 1 < abs(diff[1]):
        tail_y += 1 if 0 < diff[1] else -1
        if 0 < abs(diff[0]):
            tail_x += 1 if 0 < diff[0] else -1
    return (tail_x, tail_y)
             

def part1():
    ans = set()
    ans.add((0, 0))
    snake = [(0, 0) for _ in range(2)]
    for row in inp:
        dir, count = row.split()
        dir = directions[dir]
        for _ in range(int(count)):
            snake[0] = (snake[0][0] + dir[0], snake[0][1] + dir[1])
            for i, (head, tail) in enumerate(zip(snake, snake[1:])):
                old = tail
                snake[i + 1] = move_tail(head, tail)
            if snake[-1] != old:
                ans.add(snake[i + 1])
    submit(DAY, 1, len(ans))
            

    
def part2():
    ans = set()
    ans.add((0, 0))
    snake = [(0, 0) for _ in range(10)]
    for row in inp:
        dir, count = row.split()
        dir = directions[dir]
        for _ in range(int(count)):
            snake[0] = (snake[0][0] + dir[0], snake[0][1] + dir[1])
            for i, (head, tail) in enumerate(zip(snake, snake[1:])):
                old = tail
                snake[i + 1] = move_tail(head, tail)
            if snake[-1] != old:
                ans.add(snake[i + 1])
    submit(DAY, 2, len(ans))
                        
    
if __name__ == "__main__":
    part1() 
    part2()