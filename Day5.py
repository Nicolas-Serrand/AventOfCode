from aoc_2022 import *
import collections
import math

DAY = 5

inp = get_input(DAY).strip().split("\n")

# -- Usefull functions ----

def move(cargo, start, end):
    cargo[end].append(cargo[start][-1])
    cargo[start] = cargo[start][:-1]

def move_9001(cargo, n, start, end):
    cargo[end].extend(cargo[start][-n:])
    cargo[start] = cargo[start][:-n]

def parse_cargo(inp):
    rows_inp = []
    for row in inp:
        if not row.startswith(' 1'):
            rows_inp.append(row)
        else:
            width = max(list(map(int, row.split())))
            break
    cargo = [[] for _ in range(width)]
    rows_inp.reverse()
    for row in rows_inp:
        for i in range(width):
            if (v := row[1 + 4 * i]) != ' ':
                cargo[i].append(v)
    return cargo

# -- Main functions -----

def part1():
    cargo = parse_cargo(inp)
    for row in inp:
        if row.startswith("move"):
            row = row.split()
            n = int(row[1])
            start = int(row[3]) - 1
            end = int(row[5]) - 1
            for _ in range(n):
                move(cargo, start, end)
    ans = "".join([c[-1] for c in cargo if c])
    submit(DAY, 1, ans)

def part2():
    cargo = parse_cargo(inp)
    for row in inp:
        if row.startswith("move"):
            row = row.split()
            n = int(row[1])
            start = int(row[3]) - 1
            end = int(row[5]) - 1
            move_9001(cargo, n, start, end)
    ans = "".join([c[-1] for c in cargo if c])
    submit(DAY, 2, ans)   

if __name__ == "__main__":
    part1() 
    part2()