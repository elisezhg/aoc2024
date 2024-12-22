inputs_example = open("day22/day22_example.txt").read().split()
inputs = open("day22/day22.txt").read().split()

from collections import defaultdict


def compute(num):
    num = mixAndPrune(num * 64, num)
    num = mixAndPrune(num // 32, num)
    return mixAndPrune(num * 2048, num)


def mixAndPrune(a, num):
    return (num ^ a) % 16777216


def part1(inputs):
    it = 2000
    inputs = list(map(int, inputs))

    total = 0
    for num in inputs:
        for _ in range(it):
            num = compute(num)
        total += num

    return total


def part2(inputs):
    it = 2000
    inputs = list(map(int, inputs))

    diffsToBananas = defaultdict(int)

    for num in inputs:
        lastInt = num % 10
        seen = set()
        a1, a2, a3, a4 = None, None, None, None

        for _ in range(it):
            num = compute(num)
            currInt = num % 10

            a1, a2, a3, a4 = a2, a3, a4, currInt - lastInt

            lastInt = currInt

            if a1 is None or a2 is None or a3 is None or a4 is None:
                continue

            if (a1, a2, a3, a4) not in seen:
                diffsToBananas[(a1, a2, a3, a4)] += currInt
                seen.add((a1, a2, a3, a4))

    return max(diffsToBananas.values())


print("-------- Day 22 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
