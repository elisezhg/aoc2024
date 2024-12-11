inputs_example = open("day11/day11_example.txt").read().split(" ")
inputs = open("day11/day11.txt").read().split(" ")


def part1(inputs):
    stones = map(int, inputs)

    it = 25

    for i in range(it):
        ns = []
        for s in stones:
            if s == 0:
                ns.append(1)
            elif len(str(s)) % 2 == 0:
                s1, s2 = str(s)[: len(str(s)) // 2], str(s)[len(str(s)) // 2 :]
                s1, s2 = int(s1), int(s2)
                ns.append(s1)
                ns.append(s2)
            else:
                ns.append(s * 2024)
        stones = ns

    return len(stones)


from collections import defaultdict


def part2(inputs):
    stones = map(int, inputs)
    stonesMap = defaultdict(int)

    for s in stones:
        stonesMap[s] = 1

    it = 75

    for i in range(it):
        ns = defaultdict(int)

        for _, (s, v) in enumerate(stonesMap.items()):
            if s == 0:
                ns[1] += v
            elif len(str(s)) % 2 == 0:
                s1, s2 = str(s)[: len(str(s)) // 2], str(s)[len(str(s)) // 2 :]
                s1, s2 = int(s1), int(s2)
                ns[s1] += v
                ns[s2] += v
            else:
                ns[s * 2024] += v

        stonesMap = ns

    return sum(stonesMap.values())


print("-------- Day 11 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
