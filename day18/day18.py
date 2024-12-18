inputs_example = open("day18/day18_example.txt").read().split()
inputs = open("day18/day18.txt").read().split()

import heapq


def printGrid(grid):
    print("\n".join(["".join(g) for g in grid]))


def getNode(inputs, x, y):
    if 0 <= y < len(inputs) and 0 <= x < len(inputs[0]):
        return (x, y)
    else:
        return None


def part1(inputs, n, numBytes):
    grid = [["."] * n for i in range(n)]
    bs = [tuple(map(int, b.split(","))) for b in inputs]

    for i in range(numBytes):
        x, y = bs[i]
        grid[y][x] = "#"

    S, E = (0, 0), (n - 1, n - 1)
    # printGrid(grid)

    return findPath(grid, S, E)


def part2(inputs, n, numBytes):
    grid = [["."] * n for i in range(n)]
    bs = [tuple(map(int, b.split(","))) for b in inputs]

    for i in range(numBytes):
        x, y = bs[i]
        grid[y][x] = "#"

    S, E = (0, 0), (n - 1, n - 1)
    # printGrid(grid)

    corruptedIdx = numBytes
    while findPath(grid, S, E):
        corruptedIdx += 1
        x, y = bs[corruptedIdx]
        grid[y][x] = "#"

    return bs[corruptedIdx]


def findPath(grid, S, E):
    visited = set()
    stack = [(0, S)]

    while stack:
        steps, pos = heapq.heappop(stack)
        x, y = pos

        if pos in visited:
            continue
        else:
            visited.add(pos)

        if pos == E:
            return steps

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
                heapq.heappush(stack, (steps + 1, (nx, ny)))


print("-------- Day 18 --------")
print("Part 1:")
print(f"\t{part1(inputs_example ,7, 12)}")
print(f"\t{part1(inputs, 71, 1024)}")
print("Part 2:")
print(f"\t{part2(inputs_example, 7, 12)}")
print(f"\t{part2(inputs, 71, 1024)}")
