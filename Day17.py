from aoc_2022 import *

DAY = 17

inp = get_input(DAY).strip().splitlines()
# inp = get_example(DAY, offset=1).strip().splitlines()

blocs = [
    ["####"],

    [".#.",
     "###",
     ".#."],

    ["..#",
     "..#",
     "###"],

    ["#",
     "#",
     "#",
     "#"],

    ["##",
     "##"]
]

width = 7

grid = []

def print_grid():
    print()
    for i in range(len(grid) - 1, -1, -1):
        print("|" + "".join(grid[i]) + "|")
    print("+" + "-" * width + "+")

def solve(N):
    global grid
    instructions = inp[0].replace("&gt;", ">").replace("&lt;", "<")
    print(instructions)
    current_bloc = None
    current_bloc_height, current_bloc_width = 0, 0
    current_bloc_id = 0
    k = 0
    u = 0
    memoize_height = 0
    memoize = {}
    while k < N:
        instruction = instructions[u]
        if not current_bloc:
            key = [current_bloc_id, u]
            for j in range(width):
                i = 0
                while i < len(grid) and grid[len(grid) - i - 1][j] != "#":
                    i += 1
                key.append(i)
            key = tuple(key)
            if key in memoize:
                k0, h0 = memoize[key]
                memoize_height = h0 + ((N - k0) // (k - k0)) * (len(grid) - h0) - len(grid)
                N = (N - k0) % (k - k0)
                k = 0
                memoize.clear()
            else:
                memoize[key] = (k, len(grid))
            for _ in range(3):
                grid.append(['.' for _ in range(width)])
            current_bloc = blocs[current_bloc_id]
            current_bloc_height = len(current_bloc)
            current_bloc_width = len(current_bloc[0])
            for row in current_bloc[::-1]:
                grid.append(list(".." + row.replace('#', '@') + "." * (width - len(row) - 2)))
            current_bloc_position = [len(grid) - 1, 2]
        if instruction == "<" and 0 < current_bloc_position[1]:
            can_move = True
            for i in range(current_bloc_height):
                for j in range(current_bloc_width):
                    if current_bloc[i][j] == '#' \
                        and grid[current_bloc_position[0] - i][current_bloc_position[1] + j - 1] == '#':
                        can_move = False
            if can_move:
                for i in range(current_bloc_height):
                    grid[current_bloc_position[0] - i] = ['.' if c == '@' else c for c in grid[current_bloc_position[0] - i]]
                    for j in range(current_bloc_width):
                        if current_bloc[i][j] == '#':
                            grid[current_bloc_position[0] - i][current_bloc_position[1] + j - 1] = '@'
                current_bloc_position[1] -= 1
        elif instruction == ">" and current_bloc_position[1] + current_bloc_width < width:
            can_move = True
            for i in range(current_bloc_height):
                for j in range(current_bloc_width):
                    if current_bloc[i][j] == '#' \
                            and grid[current_bloc_position[0] - i][current_bloc_position[1] + j + 1] == '#':
                        can_move = False
            if can_move:
                for i in range(current_bloc_height):
                    grid[current_bloc_position[0] - i] = ['.' if c == '@' else c for c in grid[current_bloc_position[0] - i]]
                    for j in range(current_bloc_width):
                        if current_bloc[i][j] == '#':
                            grid[current_bloc_position[0] - i][current_bloc_position[1] + j + 1] = '@'
                current_bloc_position[1] += 1
        can_move_down = True
        if current_bloc_position[0] - current_bloc_height + 1 == 0:
            can_move_down = False
        else:
            for i in range(current_bloc_height):
                for j in range(current_bloc_width):
                    if current_bloc[i][j] == '#' \
                            and grid[current_bloc_position[0] - i - 1][current_bloc_position[1] + j] == '#':
                        can_move_down = False
        if can_move_down:
            grid[current_bloc_position[0]] = ['.' if c == '@' else c for c in grid[current_bloc_position[0]]]
            for i in range(current_bloc_height):
                grid[current_bloc_position[0] - i - 1] = ['.' if c == '@' else c for c in grid[current_bloc_position[0] - i - 1]]
                for j in range(current_bloc_width):
                    if current_bloc[i][j] == '#':
                        grid[current_bloc_position[0] - i - 1][current_bloc_position[1] + j] = '@'
            if all(c == '.' for c in grid[-1]):
                grid.pop()
            current_bloc_position[0] -= 1
        else:
            for i in range(current_bloc_height):
                grid[current_bloc_position[0] - i] = ['#' if c == '@' else c for c in grid[current_bloc_position[0] - i]]
            current_bloc = None
            current_bloc_id = (current_bloc_id + 1) % len(blocs)
            k += 1
        u = (u + 1) % len(instructions)
    return memoize_height + len(grid)

def part1():
    submit(DAY, 1, solve(2022))
def part2():
    submit(DAY, 2, solve(1_000_000_000_000))

if __name__ == "__main__":
    part1()
    part2()
