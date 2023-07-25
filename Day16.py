import itertools

from aoc_2022 import *
import math
from dataclasses import dataclass
import random


DAY = 16

inp = get_input(DAY).strip().splitlines()
# inp = get_example(DAY).strip().splitlines()

@dataclass
class Valve:
    name: str
    flow: int
    connections: list

graph = {}

memoize = {}
def solve(position: str, time: int, opened: set = set(), ignored = set()):
    key = position + str(time) + str(opened)
    if key in memoize:
        return memoize[key]
    if time == 0:
        memoize[key] = 0
        return 0
    score = sum(graph[o].flow for o in opened)
    best_score = 0
    if position not in opened and 0 < graph[position].flow and position not in ignored:
        opened.add(position)
        best_score = max(best_score, solve(position, time - 1, opened, ignored))
        opened.remove(position)
    best_score = max(best_score, max(solve(v, time - 1, opened, ignored) for v in graph[position].connections))
    memoize[key] = score +  best_score
    return score + best_score


def part1():
    for row in inp:
        row = row.split()
        name = row[1]
        flow = int(row[4].strip(';').split('=')[1])
        connections = [n.strip(',') for n in row[9:]]
        graph[name] = Valve(name, flow, connections)
    score = solve("AA", 30)
    submit(DAY, 1, score)

def part2():
    for row in inp:
        row = row.split()
        name = row[1]
        flow = int(row[4].strip(';').split('=')[1])
        connections = [n.strip(',') for n in row[9:]]
        random.shuffle(connections)
        graph[name] = Valve(name, flow, connections)

    valves_with_flow = [v.name for v in graph.values() if 0 < v.flow]
    score = 0
    n = int(math.factorial(len(valves_with_flow)) / (math.factorial(len(valves_with_flow) // 2) * math.factorial(len(valves_with_flow) - len(valves_with_flow) // 2)))
    for i, target_1 in enumerate(itertools.combinations(valves_with_flow, len(valves_with_flow) // 2)):
        target_2 = [v for v in valves_with_flow if v not in target_1]
        memoize.clear()
        score1 = solve("AA", 26, ignored=set(target_1))
        memoize.clear()
        score2 = solve("AA", 26, ignored=set(target_2))
        score = max(score, score1 + score2)
        print(f"{i} / {n}: {score}")
    submit(DAY, 2, score)


if __name__ == "__main__":
    part1()
    part2()