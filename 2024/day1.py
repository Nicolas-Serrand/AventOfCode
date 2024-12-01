data = open("input.txt").readlines()

def part_1(data):
    left = []
    right = []
    for row in data:
        a, b = row.split()
        left.append(int(a))
        right.append(int(b))
    left.sort()
    right.sort()
    result = sum((abs(a - b) for a, b in zip(left, right)))
    return result

def part_2(data):
    left = []
    right = []
    for row in data:
        a, b = row.split()
        left.append(int(a))
        right.append(int(b))
    result = sum((a * right.count(a) for a in left))
    return result

print(f"part 1 :{part_1(data)}")
print(f"part 2 :{part_2(data)}")

