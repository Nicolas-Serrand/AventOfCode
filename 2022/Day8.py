from aoc_2022 import *
import collections
import math

DAY = 8

inp = get_input(DAY).strip().splitlines()

def part1():
    ans = set()
    for i, row in enumerate(inp):
        maxi = -1
        for j, t in enumerate(row):
            t = int(t)
            if maxi < t:
                ans.add((i,j))
                maxi = max(t, maxi)
        maxi = -1
        for j, t in enumerate(row[::-1]):
            t = int(t)
            if maxi < t:
                ans.add((i,len(row)-1-j))
                maxi = max(t, maxi)
    for j in range(len(inp[0])):
        maxi = -1
        for i in range(len(inp)):
            t = int(inp[i][j])
            if maxi < t:
                ans.add((i,j))
                maxi = max(t, maxi)
        maxi = -1
        for i in range(len(inp)-1, -1, -1):
            t = int(inp[i][j])
            if maxi < t:
                ans.add((i,j))
                maxi = max(t, maxi)
    submit(DAY, 1, len(ans))
    
    
def part2():
    ans = dict()
    for a in range(len(inp)):
        for b in range(len(inp[0])):
            height = int(inp[a][b])
            ans[(a,b)] = 1
            d = 0
            for i in range(a-1, -1, -1):
                if height <= int(inp[i][b]):
                    d += 1
                    break
                d += 1
            ans[(a,b)] *= d
            d = 0
            for i in range(a+1, len(inp)):
                if height <= int(inp[i][b]):
                    d += 1
                    break
                d += 1            
            ans[(a,b)] *= d
            d = 0
            for j in range(b-1, -1, -1):
                if height <= int(inp[a][j]):
                    d += 1
                    break
                d += 1            
            ans[(a,b)] *= d    
            d = 0         
            for j in range(b+1, len(inp[0])):
                if height <= int(inp[a][j]):
                    d += 1
                    break
                d += 1            
            ans[(a,b)] *= d   
    submit(DAY, 2, max(ans.values()))
            
    
if __name__ == "__main__":
    part1() 
    part2()