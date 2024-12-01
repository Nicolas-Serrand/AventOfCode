from aoc_2022 import *
import collections
import math

DAY = 11

inp = get_input(DAY).strip().splitlines()
#inp = get_example(DAY, 0).splitlines()

class Monkey:
    def __init__(self, items, operation_line, divisible, to_true, to_false):
        self.items = items
        self.operation_line = operation_line
        self.divisible = divisible
        self.to_true = to_true
        self.to_false = to_false
    
    def operation(self, old):
        return eval(self.operation_line)

    def test(self, x):
        if x % self.divisible:
            return self.to_false
        else:
            return self.to_true
        

def part1():
    monkeys = []
    iterator = iter(inp)
    for row in iterator:
        if row.startswith("Monkey"):
            items = collections.deque(int(i) for i in next(iterator).split(':')[1].split(", "))
            operation_line = next(iterator).split('=')[1].strip()
            divisible = int(next(iterator).split()[-1])
            to_true = int(next(iterator).split()[-1])
            to_false = int(next(iterator).split()[-1])
            monkeys.append(Monkey(items, operation_line, divisible, to_true, to_false))
    counter = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                counter[i] += 1
                item = monkey.items.popleft()
                item = monkey.operation(item)
                item = item // 3
                to_monkey = monkey.test(item)
                monkeys[to_monkey].items.append(item)
    counter.sort()
    ans = counter[-1] * counter[-2]
    submit(DAY, 1, ans)

    
def part2():
    monkeys = []
    modulo = 1
    iterator = iter(inp)
    for row in iterator:
        if row.startswith("Monkey"):
            items = collections.deque(int(i) for i in next(iterator).split(':')[1].split(", "))
            operation_line = next(iterator).split('=')[1].strip()
            divisible = int(next(iterator).split()[-1])
            modulo *= divisible
            to_true = int(next(iterator).split()[-1])
            to_false = int(next(iterator).split()[-1])
            monkeys.append(Monkey(items, operation_line, divisible, to_true, to_false))
    counter = [0 for _ in range(len(monkeys))]
    for a in range(10_000):
        for i, monkey in enumerate(monkeys):
            while monkey.items:
                counter[i] += 1
                item = monkey.items.popleft()
                item = monkey.operation(item) % modulo
                to_monkey = monkey.test(item)
                monkeys[to_monkey].items.append(item)
    counter.sort()
    ans = counter[-1] * counter[-2]
    submit(DAY, 2, ans)  
    
      
if __name__ == "__main__":
    part1() 
    part2()