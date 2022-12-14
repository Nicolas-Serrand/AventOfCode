from aoc_2022 import *
import collections
import math

DAY = 14

inp = get_input(DAY).strip().splitlines()

height = 300
width = 1000
# -- Main functions -----

def part1():
    max_height = 0
    start = (500, 0)
    grid = [['.' for _ in range(height)] for _ in range(width)]
    grid[start[0]][start[1]] = '+'
    for row in inp:
        points = [tuple(int(i) for i in p.split(',')) for p in row.split('->')]
        for (p1_x, p1_y), (p2_x, p2_y) in zip(points, points[1:]):
            if p1_x == p2_x:
                for y in range(min(p1_y, p2_y), max(p1_y, p2_y) + 1):
                    grid[p1_x][y] = '#'
            elif p1_y == p2_y:
                for x in range(min(p1_x, p2_x), max(p1_x, p2_x) + 1):
                    grid[x][p1_y] = '#'
        grid[points[-1][0]][points[-1][1]] = '#'
        max_height = max(max_height, *(p[1] for p in points))
    counter = 0
    sand = start
    while sand[1] <= 2*max_height:
        if grid[sand[0]][sand[1] + 1] == '.':
            sand = (sand[0], sand[1] + 1)
        elif grid[sand[0] - 1][sand[1] + 1] == '.':
            sand = (sand[0] - 1, sand[1] + 1)
        elif grid[sand[0] + 1][sand[1] + 1] == '.':
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            grid[sand[0]][sand[1]] = 'o'
            sand = start
            counter += 1
    submit(DAY, 1, counter)

    

def part2():
    max_height = 0
    start = (500, 0)
    grid = [['.' for _ in range(height)] for _ in range(width)]
    grid[start[0]][start[1]] = '+'
    for row in inp:
        points = [tuple(int(i) for i in p.split(',')) for p in row.split('->')]
        for (p1_x, p1_y), (p2_x, p2_y) in zip(points, points[1:]):
            if p1_x == p2_x:
                for y in range(min(p1_y, p2_y), max(p1_y, p2_y) + 1):
                    grid[p1_x][y] = '#'
            elif p1_y == p2_y:
                for x in range(min(p1_x, p2_x), max(p1_x, p2_x) + 1):
                    grid[x][p1_y] = '#'
        grid[points[-1][0]][points[-1][1]] = '#'
        max_height = max(max_height, *(p[1] for p in points))
    for x in range(width):
        grid[x][max_height + 2] = '#' 
    counter = 0
    sand = start
    while True:
        if grid[sand[0]][sand[1] + 1] == '.':
            sand = (sand[0], sand[1] + 1)
        elif grid[sand[0] - 1][sand[1] + 1] == '.':
            sand = (sand[0] - 1, sand[1] + 1)
        elif grid[sand[0] + 1][sand[1] + 1] == '.':
            sand = (sand[0] + 1, sand[1] + 1)
        elif grid[sand[0]][sand[1]] == '.':
            grid[sand[0]][sand[1]] = 'o'
            sand = start
            counter += 1
        else:
            grid[sand[0]][sand[1]] = 'o'
            counter += 1
            break
    submit(DAY, 2, counter)    

if __name__ == "__main__":
    #part1() 
    part2()