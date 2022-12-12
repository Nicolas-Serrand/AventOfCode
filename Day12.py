from aoc_2022 import *
import collections
import math

DAY = 12

inp = get_input(DAY).strip().splitlines()

# inp = """
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.strip().splitlines()

def part1():
    grid = [list(row) for row in inp]
    start, end = None, None
    height, width = len(grid), len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 'S':
                start = (x, y)
                grid[x][y] = 0
            elif grid[x][y] == 'E':
                end = (x, y)
                grid[x][y] = 25
            else:
                grid[x][y] = ord(grid[x][y]) - 97
    seen = set()
    seen.add(start)
    queue = collections.deque()
    queue.append((start, 0))
    ans = None
    while queue:
        current, dist = queue.popleft()
        if current == end:
            ans = dist
            break
        current_x, current_y = current
        current_v = grid[current_x][current_y]
        for m, n in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = current_x + m
            next_y = current_y + n
            if (next_x, next_y) not in seen \
                and 0 <= next_x \
                and next_x < height \
                and 0 <=  next_y \
                and  next_y < width \
                and grid[next_x][next_y] - current_v <= 1:
                seen.add((next_x, next_y))
                queue.append(((next_x, next_y), dist + 1))
    submit(DAY, 1, ans)
                
            

    
def part2():
    grid = [list(row) for row in inp]
    start, end = None, None
    height, width = len(grid), len(grid[0])
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 'S':
                start = (x, y)
                grid[x][y] = 0
            elif grid[x][y] == 'E':
                end = (x, y)
                grid[x][y] = 25
            else:
                grid[x][y] = ord(grid[x][y]) - 97
    start, end = end, start
    seen = set()
    seen.add(start)
    queue = collections.deque()
    queue.append((start, 0))
    ans = None
    while queue:
        current, dist = queue.popleft()
        current_x, current_y = current
        current_v = grid[current_x][current_y]
        if current_v == 0:
            ans = dist
            break
        for m, n in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_x = current_x + m
            next_y = current_y + n
            if (next_x, next_y) not in seen \
                and 0 <= next_x \
                and next_x < height \
                and 0 <=  next_y \
                and  next_y < width \
                and grid[next_x][next_y] - current_v >= -1:
                seen.add((next_x, next_y))
                queue.append(((next_x, next_y), dist + 1))
    submit(DAY, 2, ans)
                    
      
if __name__ == "__main__":
    part1() 
    part2()