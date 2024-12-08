inputs_example = open("day08/day08_example.txt").read().split("\n")
inputs = open("day08/day08.txt").read().split("\n")

from collections import defaultdict
from itertools import combinations


def getNextPos(grid, pos, dir):
    newX, newY = (pos[0] + dir[0], pos[1] + dir[1])

    if newX < 0 or newX >= len(grid[0]):
        return None

    if newY < 0 or newY >= len(grid):
        return None

    return newX, newY


def part1(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for i in inputs]

    charsMap = defaultdict(list)

    for x in range(m):
        for y in range(n):
            c = grid[x][y]
            if c != ".":
                charsMap[c].append((x, y))

    for coords in charsMap.values():
        combs = list(combinations(coords, 2))
        for (x0, y0), (x1, y1) in combs:
            diff = (x0 - x1, y0 - y1)
            diff2 = (-diff[0], -diff[1])
            positions = [
                getNextPos(grid, (x0, y0), diff),
                getNextPos(grid, (x0, y0), diff2),
                getNextPos(grid, (x1, y1), diff),
                getNextPos(grid, (x1, y1), diff2),
            ]
            for pos in positions:
                if pos and pos != (x0, y0) and pos != (x1, y1):
                    visited[pos[0]][pos[1]] = True

    total = 0

    for y in range(m):
        line = ""
        for x in range(n):
            if visited[y][x]:
                line += "X"
                total += 1
            else:
                line += grid[y][x]
        # print(line)
    return total


def part2(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for i in inputs]

    charsMap = defaultdict(list)

    for x in range(m):
        for y in range(n):
            c = grid[x][y]
            if c != ".":
                charsMap[c].append((x, y))

    for coords in charsMap.values():
        combs = list(combinations(coords, 2))

        for (x0, y0), (x1, y1) in combs:
            diff = (x0 - x1, y0 - y1)
            diff2 = (-diff[0], -diff[1])
            positions = []

            for i in range(55):
                positions.append(
                    getNextPos(grid, (x0, y0), (diff[0] * i, diff[1] * i)),
                )
                positions.append(
                    getNextPos(grid, (x0, y0), (diff2[0] * i, diff2[1] * i)),
                )

                positions.append(
                    getNextPos(grid, (x1, y1), (diff[0] * i, diff[1] * i)),
                )

                positions.append(
                    getNextPos(grid, (x1, y1), (diff2[0] * i, diff2[1] * i)),
                )

            for pos in positions:
                if pos:
                    visited[pos[0]][pos[1]] = True

    total = 0

    for y in range(m):
        line = ""
        for x in range(n):
            if visited[y][x]:
                line += "X"
                total += 1
            else:
                line += grid[y][x]
        # print(line)
    return total


print("-------- Day 08 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
