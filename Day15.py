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
    pass    

if __name__ == "__main__":
    part1() 
    part2()