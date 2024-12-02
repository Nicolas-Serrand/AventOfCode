data = open("input.txt").readlines()

def part_1(data):
    count = 0
    for row in data:
        levels = [int(i) for i in row.split()]
        if levels[0] < levels[1]:
            for a, b in zip(levels, levels[1:]):
                if not (1 <= b - a <= 3):
                    break
            else:
                count += 1
        if levels[1] < levels[0]:
            for a, b in zip(levels, levels[1:]):
                if not (1 <= a - b <= 3):
                    break
            else:
                count += 1
    return count
            
def part_2(data):
    count = 0
    for row in data:
        levels = [int(i) for i in row.split()]
        for i in range(len(levels)):
            c_levels = levels[:i] + levels[i+1:]
            if c_levels[0] < c_levels[1]:
                for a, b in zip(c_levels, c_levels[1:]):
                    if not (1 <= b - a <= 3):
                        break
                else:
                    count += 1
                    break
            if c_levels[1] < c_levels[0]:
                for a, b in zip(c_levels, c_levels[1:]):
                    if not (1 <= a - b <= 3):
                        break
                else:
                    count += 1
                    break

    return count
print(f"part 1: {part_1(data)}")
print(f"part 2: {part_2(data)}")

