inputs_example = open("day19/day19_example.txt").read().split("\n\n")
inputs = open("day19/day19.txt").read().split("\n\n")

import sys
from functools import cache

sys.setrecursionlimit(1000000)


@cache
def isPossible(design, patterns):
    if not design:
        return True

    for p in patterns:
        if design.startswith(p):
            if isPossible(design[len(p) :], patterns):
                return True

    return False


@cache
def getPossibilities(design, patterns):
    if not design:
        return 1

    total = 0
    for p in patterns:
        if design.startswith(p):
            total += getPossibilities(design[len(p) :], patterns)

    return total


def part1(inputs):
    ts, ds = inputs
    ts = tuple(ts.split(", "))
    ds = ds.split()

    total = 0

    for d in ds:
        if isPossible(d, ts):
            total += 1

    return total


def part2(inputs):
    ts, ds = inputs
    ts = tuple(ts.split(", "))
    ds = ds.split()

    total = 0

    for d in ds:
        total += getPossibilities(d, ts)

    return total


print("-------- Day 19 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
