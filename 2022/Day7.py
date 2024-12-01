from aoc_2022 import *
import collections
import math

DAY = 7

inp = get_input(DAY).strip().split("\n")

# -- Usefull functions ----

def parse_inp(inp):
    root = {'/':{}}
    pwd = []
    for row in inp:
        if row.startswith('$'):
            row = row.split()
            if row[1] == "cd":
                if row[2] == '..':
                    pwd = pwd[:-1]
                else:
                    pwd.append(row[2])
            if row[1] == "ls":
                continue
        else:
            directory = root
            for dir in pwd:
                directory = directory[dir]
            row = row.split()
            if row[0] == "dir":
                directory[row[1]] = {}
            elif row[0].isdigit():
                directory[row[1]] = int(row[0])
    return root

def search_folders(folder, max_size=float("+inf")):
    s = 0
    ans = []
    for item in folder.values():
        if isinstance(item, dict):
            subsize, subfolders = search_folders(item, max_size)
            ans.extend(subfolders)
            s +=  subsize
        if isinstance(item, int):
            s += item
    if s <= max_size:
        ans.append(s)
    return s, ans

# -- Main functions -----

def part1():
    root = parse_inp(inp)
    max_size = 100000
    ans = sum(search_folders(root, max_size)[1])
    submit(DAY, 1, ans)


def part2():
    root = parse_inp(inp)
    total_disk = 70000000
    unused_require = 30000000
    total_used, folders = search_folders(root)
    min_to_delete = unused_require - (total_disk - total_used)
    for size in sorted(folders):
        if min_to_delete <= size:
            submit(DAY, 2, size)
            return

    
if __name__ == "__main__":
    part1() 
    part2()