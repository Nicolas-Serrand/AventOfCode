from aoc_2022 import *
from collections import  deque

DAY = 18

inp = get_input(DAY).strip().splitlines()
# inp = get_example(DAY).strip().splitlines()

size_space = 100

def part1():
    cubes = [tuple(map(int, row.split(','))) for row in inp]
    spaces = [[[False for _ in range(size_space)] for _ in range(size_space)] for _ in range(size_space)]
    answer = 0
    for x_cube, y_cube, z_cube in cubes:
        to_add = 6
        for x_delta, y_delta, z_delta in ((-1, 0, 0), (1, 0, 0),
                                          (0, -1, 0), (0, 1, 0),
                                          (0, 0, -1), (0, 0, 1)):
            if spaces[x_cube + x_delta][y_cube + y_delta][z_cube + z_delta]:
                answer -= 1
                to_add -= 1
        spaces[x_cube][y_cube][z_cube] = True
        answer += to_add
    submit(DAY, 1, answer)


def part2():
    cubes = [tuple(map(int, row.split(','))) for row in inp]
    space = [[[False for _ in range(100)] for _ in range(100)] for _ in range(100)]
    answer = 0
    for x_cube, y_cube, z_cube in cubes:
        to_add = 6
        for x_delta, y_delta, z_delta in ((-1, 0, 0), (1, 0, 0),
                                          (0, -1, 0), (0, 1, 0),
                                          (0, 0, -1), (0, 0, 1)):
            if space[x_cube + x_delta][y_cube + y_delta][z_cube + z_delta]:
                answer -= 1
                to_add -= 1
        space[x_cube][y_cube][z_cube] = True
        answer += to_add
    seen = set()
    for x in range(size_space):
        for y in range(size_space):
            for z in range(size_space):
                if not space[x][y][z] and (x, y, z) not in seen:
                    queue = deque()
                    queue.append((x, y, z))
                    seen.add((x, y, z))
                    lava_in_contact = 0
                    is_closed = True
                    while queue:
                        xq, yq, zq = queue.popleft()
                        for x_delta, y_delta, z_delta in ((-1, 0, 0), (1, 0, 0),
                                                          (0, -1, 0), (0, 1, 0),
                                                          (0, 0, -1), (0, 0, 1)):
                            if 0 <= xq + x_delta < size_space \
                                    and 0 <= yq + y_delta < size_space \
                                    and 0 <= zq + z_delta < size_space:
                                if not space[xq + x_delta][yq + y_delta][zq + z_delta]:
                                    if (xq + x_delta, yq + y_delta, zq + z_delta) not in seen:
                                        queue.append((xq + x_delta, yq + y_delta, zq + z_delta))
                                        seen.add((xq + x_delta, yq + y_delta, zq + z_delta))
                                else:
                                    lava_in_contact += 1
                            else:
                                is_closed = False
                    if is_closed:
                        answer -= lava_in_contact
    print("answer:", answer)
    submit(DAY, 2, answer)

if __name__ == "__main__":
    part1()
    part2()
