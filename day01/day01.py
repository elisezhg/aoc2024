inputs_example = open("day01/day01_example.txt").read().split("\n")
inputs = open("day01/day01.txt").read().split("\n")


def part1(inputs):
    l, r = [], []

    for i in inputs:
        chars = i.split()
        l.append(int(chars[0]))
        r.append(int(chars[1]))

    l.sort()
    r.sort()

    total = 0
    for idx in range(len(l)):
        total += abs(int(l[idx]) - r[idx])
    return total


def part2(inputs):
    l, r = [], []

    for i in inputs:
        chars = i.split()
        l.append(int(chars[0]))
        r.append(int(chars[1]))

    l.sort()

    total = 0
    for idx in range(len(l)):
        total += l[idx] * r.count(l[idx])
    return total


print("-------- Day 1 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
