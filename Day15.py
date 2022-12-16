from aoc_2022 import *
import collections
import math

DAY = 15

inp = get_input(DAY).strip().splitlines()
#inp = get_example(DAY).strip().splitlines()

def part1():
    line = 2000000
    sensors = set()
    beacons = set()
    connect = {}
    for row in inp:
        row = row.split()
        s_x = int(row[2].split('=')[1].strip(",:"))
        s_y = int(row[3].split('=')[1].strip(",:"))
        b_x = int(row[-2].split('=')[1].strip(",:"))
        b_y = int(row[-1].split('=')[1].strip(",:"))
        beacon = (b_x, b_y)
        sensor = (s_x, s_y)
        beacons.add(beacon)
        sensors.add(sensor)
        connect[sensor] = beacon
    ans = set()
    for s, b in connect.items():
        d = abs(b[0] - s[0]) + abs(b[1] - s[1])
        a = d - abs(line - s[1])
        for x in range(s[0] - a, s[0] + a + 1):
            if (x, line) not in sensors and (x, line) not in beacons: 
                ans.add((x, line))
    submit(DAY, 1, len(ans))
            
    
        
        
def part2():
    size = 4000000
    limits = [[] for _ in range(size)]
    sensors = set()
    beacons = set()
    connect = {}
    for row in inp:
        row = row.split()
        s_x = int(row[2].split('=')[1].strip(",:"))
        s_y = int(row[3].split('=')[1].strip(",:"))
        b_x = int(row[-2].split('=')[1].strip(",:"))
        b_y = int(row[-1].split('=')[1].strip(",:"))
        beacon = (b_x, b_y)
        sensor = (s_x, s_y)
        beacons.add(beacon)
        sensors.add(sensor)
        connect[sensor] = beacon
    for s, b in connect.items():
        d = abs(b[0] - s[0]) + abs(b[1] - s[1])
        for y in range(max(0, s[1] - d), min(s[1] + d + 1, size)):
            p = d - abs(s[1] - y)
            x_1 = s[0] - p
            x_2 = s[0] + p
            limits[y].append((x_1, x_2))
    for y, intervals in enumerate(limits):
        intervals.sort()
        i = list(intervals[0])
        for j in intervals[1:]:
            if j[0] <= i[1] + 1:
                i[1] = max(i[1], j[1])
            else:
                submit(DAY, 2, (j[0] - 1) * size + y)
                return

    
if __name__ == "__main__":
    part1() 
    part2()