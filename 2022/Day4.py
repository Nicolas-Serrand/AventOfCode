from aoc_2022 import *
import collections
import math

DAY = 4

inp = get_input(DAY).strip().split("\n")


def part1():
    ans = 0
    for row in inp:
        first_elf, second_elf = row.split(',')
        f_a, f_b = list(map(int, first_elf.split(('-'))))
        s_a, s_b = list(map(int, second_elf.split(('-'))))
        if (f_a <= s_a and s_b <= f_b) or (s_a <= f_a and f_b <= s_b):
            ans += 1
    submit(DAY, 1, ans)
    
def part2():
    ans = 0
    for row in inp:
        first_elf, second_elf = row.split(',')
        f_a, f_b = list(map(int, first_elf.split(('-'))))
        s_a, s_b = list(map(int, second_elf.split(('-'))))
        if (f_a <= s_a and s_a <= f_b) or (f_a <= s_b and s_b <= f_b) or (s_a <= f_a and f_a <= s_b):
            ans += 1
    submit(DAY, 2, ans)
                

if __name__ == "__main__":
    part1() 
    part2()