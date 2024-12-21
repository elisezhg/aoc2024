inputs_example = open("day21/day21_example.txt").read().split("\n")
inputs = open("day21/day21.txt").read().split("\n")

import heapq
import math
from functools import cache

NUM_PAD = "789/456/123/ 0A"
NUM_PAD = tuple([tuple(i) for i in NUM_PAD.split("/")])


DIR_PAD = " ^A/<v>"
DIR_PAD = tuple([tuple(i) for i in DIR_PAD.split("/")])


@cache
def getIdx(grid, char):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == char:
                return (i, j)


@cache
def getNode(inputs, idx):
    (x, y), d = idx
    if 0 <= y < len(inputs) and 0 <= x < len(inputs[0]):
        return (x, y), d
    else:
        return None


@cache
def findPath(grid, S, E):
    stack = [(0, S, [])]
    possibilities = []
    minSteps = math.inf

    while stack:
        steps, pos, path = heapq.heappop(stack)
        x, y = pos

        if steps > minSteps:
            break

        if pos == E:
            possibilities.append("".join(path) + "A")
            minSteps = min(minSteps, steps)
            continue

        possibleIdx = [
            ((x, y + 1), "v"),
            ((x - 1, y), "<"),
            ((x + 1, y), ">"),
            ((x, y - 1), "^"),
        ]

        possibleNodes = [getNode(grid, idx) for idx in possibleIdx]
        possibleNodes = [n for n in possibleNodes if n is not None]
        for (nx, ny), d in possibleNodes:
            if grid[ny][nx] != " ":
                heapq.heappush(stack, (steps + 1, (nx, ny), path + [d]))

    return [p for p in possibilities if len(p) == minSteps + 1]


@cache
def findSequence(code, depth, pad=DIR_PAD):
    if depth == 0:
        return len(code)

    currentIdx = getIdx(pad, "A")
    total = 0

    for char in code:
        targetIdx = getIdx(pad, char)
        path = findPath(pad, currentIdx, targetIdx)
        total += min(findSequence(p, depth - 1) for p in path)
        currentIdx = targetIdx

    return total


def part1(inputs):
    return sum([findSequence(code, 3, NUM_PAD) * int(code[:-1]) for code in inputs])


def part2(inputs):
    return sum([findSequence(code, 26, NUM_PAD) * int(code[:-1]) for code in inputs])


print("-------- Day 21 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
# print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
