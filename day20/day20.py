inputs_example = open("day20/day20_example.txt").read().split("\n")
inputs = open("day20/day20.txt").read().split("\n")

import heapq
from collections import defaultdict


def getNode(inputs, x, y):
    if 0 <= y < len(inputs) and 0 <= x < len(inputs[0]):
        return (x, y)
    else:
        return None


def getTime(grid, S, E):
    visited = set()
    stack = [(0, S, [S])]

    while stack:
        steps, pos, path = heapq.heappop(stack)
        x, y = pos

        if pos in visited:
            continue
        else:
            visited.add(pos)

        if pos == E:
            return path

        possibleIdx = [
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
        ]

        possibleNodes = [getNode(grid, *idx) for idx in possibleIdx]
        possibleNodes = [n for n in possibleNodes if n is not None]
        for nx, ny in possibleNodes:
            if grid[ny][nx] != "#":
                heapq.heappush(stack, (steps + 1, (nx, ny), path + [(nx, ny)]))


def getTimesWithCheats(grid, E, path):
    stack = []

    visited = set()
    for i, p in enumerate(path):
        heapq.heappush(stack, (i, p, visited.copy(), False))
        visited.add(p)

    possibilities = defaultdict(int)

    while stack:
        steps, pos, visited, cheatUsed = heapq.heappop(stack)
        x, y = pos

        if pos in visited:
            continue
        else:
            visited.add(pos)

        if cheatUsed and grid[y][x] != "#":
            if pos in path:
                idxWithoutCheat = path.index(pos)
                saved = idxWithoutCheat - steps
                possibilities[saved] += 1
                continue

        if pos == E:
            possibilities[len(path) - steps] += 1
            continue

        possibleIdx = [
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
        ]

        possibleNodes = [getNode(grid, *idx) for idx in possibleIdx]
        possibleNodes = [n for n in possibleNodes if n is not None]
        for nx, ny in possibleNodes:
            canUseCheat = not cheatUsed and grid[ny][nx] == "#"
            backOnTrack = cheatUsed and grid[ny][nx] != "#"
            if canUseCheat or backOnTrack:
                heapq.heappush(stack, (steps + 1, (nx, ny), visited.copy(), True))

    return possibilities


def part1(inputs, minSavedSecs):
    grid = [list(i) for i in inputs]

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "S":
                S = (j, i)
            elif c == "E":
                E = (j, i)

    path = getTime(grid, S, E)
    times = getTimesWithCheats(grid, E, path)

    total = 0
    for savedSecs, count in sorted(times.items()):
        # print(savedSecs, count)
        if savedSecs >= minSavedSecs:
            total += count

    return total


def part2(inputs, minSavedSecs):
    grid = [list(i) for i in inputs]

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == "S":
                S = (j, i)
            elif c == "E":
                E = (j, i)

    path = getTime(grid, S, E)
    savedTimes = defaultdict(int)

    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            savedTimes[getSavedTime(i, j, path, 20)] += 1

    total = 0
    for savedSecs, count in sorted(savedTimes.items()):
        if savedSecs >= minSavedSecs:
            total += count

    return total


def getSavedTime(si, ei, path, maxCheats):
    (sx, sy), (ex, ey) = path[si], path[ei]
    cheatDistance = abs(sx - ex) + abs(sy - ey)
    return ei - si - cheatDistance if cheatDistance <= maxCheats else -1


print("-------- Day 20 --------")
print("Part 1:")
print(f"\t{part1(inputs_example, 2)}")
print(f"\t{part1(inputs, 100)}")
print("Part 2:")
print(f"\t{part2(inputs_example, 50)}")
print(f"\t{part2(inputs, 100)}")
