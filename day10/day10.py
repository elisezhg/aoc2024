inputs_example = open("day10/day10_example.txt").read().split()
inputs = open("day10/day10.txt").read().split()

import operator


def part1(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])

    ths = set()

    for i in range(n):
        for j in range(m):
            curr = grid[i][j]
            if curr == "0":
                ths.add((j, i))

    total = 0
    for th in ths:
        thTotal = 0
        visited = set()
        stack = [th]

        while stack:
            x, y = stack.pop()

            if (x, y) not in visited:
                visited.add((x, y))

                LEFT = (-1, 0)
                RIGHT = (1, 0)
                UP = (0, -1)
                DOWN = (0, 1)
                possibleDirs = [LEFT, RIGHT, UP, DOWN]
                possibleIdx = []

                for d in possibleDirs:
                    newIdx = list(map(operator.add, (x, y), d))
                    possibleIdx.append([newIdx[0], newIdx[1]])

                for node in possibleIdx:
                    newX, newY = node

                    if 0 <= newX < n and 0 <= newY < m:
                        if (
                            grid[newY][newX].isdigit()
                            and int(grid[newY][newX]) == int(grid[y][x]) + 1
                        ):
                            stack.append((newX, newY))
                            if (
                                int(grid[newY][newX]) == 9
                                and (newX, newY) not in visited
                            ):
                                thTotal += 1

        total += thTotal

    return total


def part2(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])

    ths = set()

    for i in range(n):
        for j in range(m):
            curr = grid[i][j]
            if curr == "0":
                ths.add((j, i))

    total = 0
    for th in ths:
        thTotal = 0
        stack = [th]

        while stack:
            x, y = stack.pop()

            LEFT = (-1, 0)
            RIGHT = (1, 0)
            UP = (0, -1)
            DOWN = (0, 1)
            possibleDirs = [LEFT, RIGHT, UP, DOWN]
            possibleIdx = []

            for d in possibleDirs:
                newIdx = list(map(operator.add, (x, y), d))
                possibleIdx.append([newIdx[0], newIdx[1]])

            for node in possibleIdx:
                newX, newY = node

                if 0 <= newX < n and 0 <= newY < m:
                    if (
                        grid[newY][newX].isdigit()
                        and int(grid[newY][newX]) == int(grid[y][x]) + 1
                    ):
                        stack.append((newX, newY))
                        if int(grid[newY][newX]) == 9:
                            thTotal += 1

        total += thTotal
    return total


print("-------- Day 10 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
