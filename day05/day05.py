inputs_example = open("day05/day05_example.txt").read().split("\n\n")
inputs = open("day05/day05.txt").read().split("\n\n")
from collections import defaultdict


def part1(inputs):
    _rules, updates = inputs[0].split("\n"), inputs[1].split("\n")

    befores = defaultdict(list)
    for r in _rules:
        [a, b] = r.split("|")
        befores[int(b)].append(int(a))

    total = 0
    for update in updates:
        valid = True
        update = update.split(",")
        update = [int(i) for i in update]

        seen = []

        for num in update:
            # all in seen must be in before
            for s in seen:
                if s not in befores[num]:
                    valid = False
                    break
            seen.append(num)

            if not valid:
                break

        if valid:
            total += update[int((len(update) - 1) / 2)]

    return total


def part2(inputs):
    _rules, updates = inputs[0].split("\n"), inputs[1].split("\n")
    befores = defaultdict(list)

    for r in _rules:
        [a, b] = r.split("|")
        befores[int(b)].append(int(a))

    invalids = []
    for update in updates:
        valid = True
        update = update.split(",")
        update = [int(i) for i in update]

        seen = []

        for num in update:
            # all in seen must be in before
            for s in seen:
                if s not in befores[num]:
                    valid = False
                    break
            seen.append(num)

            if not valid:
                break

        if not valid:
            invalids.append(update)

    total = 0

    for nums in invalids:
        corrected = correct(nums, befores)
        total += corrected[int((len(corrected) - 1) / 2)]

    return total


def correct(nums, befores):
    notSeen = [n for n in nums]
    corrected = []

    while notSeen:
        for n in notSeen:
            valid = True
            for i in befores[n]:
                if i in notSeen:
                    valid = False
                    break
            if valid:
                corrected.append(n)
                notSeen.remove(n)

    return corrected


print("-------- Day 05 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
