inputs_example = open("day15/day15_example.txt").read().split("\n\n")
inputs = open("day15/day15.txt").read().split("\n\n")

import copy


def slideNorth(grid, pos):
    c, y = pos
    newGrid = [list(g) for g in grid]
    for r in range(y, -1, -1):
        if newGrid[r][c] == "O":
            found = False
            newR = r - 1
            while (
                not found
                and newR >= 0
                and (newGrid[newR][c] == "." or newGrid[newR][c] == "O")
            ):
                if newGrid[newR][c] == "O":
                    newGrid = slideNorth(newGrid, (c, newR))
                if newGrid[newR][c] == "O":
                    return newGrid
                found = True
                newR -= 1
            if found:
                newGrid[newR + 1][c] = "O"
                newGrid[r][c] = "."
                return newGrid
    return newGrid


def slideSouth(grid, pos):
    c, y = pos
    newGrid = [list(g) for g in grid]

    for r in range(y, len(newGrid)):
        if newGrid[r][c] == "O":
            found = False
            newR = r + 1
            while (
                not found
                and newR < len(newGrid)
                and (newGrid[newR][c] == "." or newGrid[newR][c] == "O")
            ):
                if newGrid[newR][c] == "O":
                    newGrid = slideSouth(newGrid, (c, newR))
                if newGrid[newR][c] == "O":
                    return newGrid
                found = True
                newR += 1
            if found:
                newGrid[newR - 1][c] = "O"
                newGrid[r][c] = "."
                return newGrid
    return newGrid


def slideWest(grid, pos):
    x, r = pos
    newGrid = [list(g) for g in grid]

    for c in range(x, -1, -1):
        if newGrid[r][c] == "O":
            found = False
            newC = c - 1
            while (
                not found
                and newC >= 0
                and (newGrid[r][newC] == "." or newGrid[r][newC] == "O")
            ):
                if newGrid[r][newC] == "O":
                    newGrid = slideWest(newGrid, (newC, r))
                if newGrid[r][newC] == "O":
                    return newGrid
                found = True
                newC -= 1
            if found:
                newGrid[r][newC + 1] = "O"
                newGrid[r][c] = "."
                return newGrid

    return newGrid


def slideEast(grid, pos):
    x, r = pos
    newGrid = [list(g) for g in grid]

    for c in range(x, len(grid[0])):
        if newGrid[r][c] == "O":
            found = False
            newC = c + 1
            while (
                not found
                and newC < len(newGrid[0])
                and (newGrid[r][newC] == "." or newGrid[r][newC] == "O")
            ):
                if newGrid[r][newC] == "O":
                    newGrid = slideEast(newGrid, (newC, r))
                if newGrid[r][newC] == "O":
                    return newGrid
                found = True
                newC += 1
            if found:
                newGrid[r][newC - 1] = "O"
                newGrid[r][c] = "."
                return newGrid

    return newGrid


def slideNorth2(grid, pos):
    c, y = pos
    newGrid = [list(g) for g in grid]
    for r in range(y, -1, -1):
        if newGrid[r][c] in "[]":
            char = newGrid[r][c]
            otherC = c - 1 if char == "]" else c + 1

            found = False
            newR = r - 1
            while (
                not found
                and newR >= 0
                and (
                    (newGrid[newR][c] == "." and newGrid[newR][otherC] == ".")
                    or newGrid[newR][c] in "[]"
                    or newGrid[newR][otherC] in "[]"
                )
            ):
                if newGrid[newR][c] in "[]":
                    newGrid = slideNorth2(newGrid, (c, newR))
                if newGrid[newR][otherC] in "[]":
                    newGrid = slideNorth2(newGrid, (otherC, newR))

                if newGrid[newR][c] in "[]#" or newGrid[newR][otherC] in "[]#":
                    return newGrid

                found = True
                newR -= 1
            if found:
                newGrid[newR + 1][c] = char
                newGrid[r][c] = "."

                newGrid[newR + 1][otherC] = "[" if char == "]" else "]"
                newGrid[r][otherC] = "."

                return newGrid
    return newGrid


def slideSouth2(grid, pos):
    c, y = pos
    newGrid = [list(g) for g in grid]

    for r in range(y, len(newGrid)):
        if newGrid[r][c] in "[]":
            char = newGrid[r][c]
            otherC = c - 1 if char == "]" else c + 1

            found = False
            newR = r + 1
            while (
                not found
                and newR < len(newGrid)
                and (
                    (newGrid[newR][c] == "." and newGrid[newR][otherC] == ".")
                    or newGrid[newR][c] in "[]"
                    or newGrid[newR][otherC] in "[]"
                )
            ):
                if newGrid[newR][c] in "[]":
                    newGrid = slideSouth2(newGrid, (c, newR))
                if newGrid[newR][otherC] in "[]":
                    newGrid = slideSouth2(newGrid, (otherC, newR))

                if newGrid[newR][c] in "[]#" or newGrid[newR][otherC] in "[]#":
                    return newGrid

                found = True
                newR += 1
            if found:
                newGrid[newR - 1][c] = char
                newGrid[r][c] = "."

                newGrid[newR - 1][otherC] = "[" if char == "]" else "]"
                newGrid[r][otherC] = "."

                return newGrid
    return newGrid


def slideWest2(grid, pos):
    x, r = pos
    newGrid = [list(g) for g in grid]

    for c in range(x, -1, -1):
        if newGrid[r][c] in "[]":
            found = False
            newC = c - 2
            while (
                not found
                and newC >= 0
                and (newGrid[r][newC] == "." or newGrid[r][newC] in "[]")
            ):
                if newGrid[r][newC] in "[]":
                    newGrid = slideWest2(newGrid, (newC, r))

                if newGrid[r][newC] in "[]#":
                    return newGrid

                found = True
                newC -= 1
            if found:
                newGrid[r][newC + 1] = "["
                newGrid[r][newC + 2] = "]"
                newGrid[r][c] = "."
                return newGrid

    return newGrid


def slideEast2(grid, pos):
    x, r = pos
    newGrid = [list(g) for g in grid]

    for c in range(x, len(grid[0])):
        if newGrid[r][c] in "[]":
            found = False
            newC = c + 2
            while (
                not found
                and newC < len(newGrid[0])
                and (newGrid[r][newC] == "." or newGrid[r][newC] in "[]")
            ):
                if newGrid[r][newC] in "[]":
                    newGrid = slideEast2(newGrid, (newC, r))

                if newGrid[r][newC] in "[]#":
                    return newGrid

                found = True
                newC += 1
            if found:
                newGrid[r][newC - 1] = "]"
                newGrid[r][newC - 2] = "["
                newGrid[r][c] = "."
                return newGrid

    return newGrid


def getNextPos(grid, pos, dir):
    newX, newY = (pos[0] + dir[0], pos[1] + dir[1])

    if newX < 0 or newX >= len(grid[0]):
        return None

    if newY < 0 or newY >= len(grid):
        return None

    return newX, newY


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

dirMap = {
    "^": (UP, slideNorth, slideNorth2),
    "<": (LEFT, slideWest, slideWest2),
    ">": (RIGHT, slideEast, slideEast2),
    "v": (DOWN, slideSouth, slideSouth2),
}


def part1(inputs):
    grid = [list(i) for i in inputs[0].split("\n")]
    ds = "".join(inputs[1].split("\n"))
    n = len(grid)
    m = len(grid[0])

    s = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                s = (j, i)

    t = 0

    for d in ds:
        dir, slide, _ = dirMap[d]
        np = getNextPos(grid, s, dir)

        if np:
            newGrid = copy.deepcopy(grid)
            if newGrid[np[1]][np[0]] != ".":
                newGrid = slide(grid, np)
            if newGrid[np[1]][np[0]] == ".":
                newGrid[np[1]][np[0]] = "@"
                newGrid[s[1]][s[0]] = "."
                grid = newGrid
                s = np

    for i in range(n):
        print("".join(grid[i]))
        for j in range(m):
            if grid[i][j] == "O":
                t += i * 100 + j
    return t


def part2(inputs):
    grid = [list(i) for i in inputs[0].split("\n")]
    expandedGrid = []
    for line in grid:
        newLine = []
        for c in line:
            if c == "@":
                newLine.append(c)
                newLine.append(".")
            elif c == "O":
                newLine.append("[")
                newLine.append("]")
            else:
                newLine.append(c)
                newLine.append(c)
        expandedGrid.append(newLine)

    grid = expandedGrid
    # print("\n".join(["".join(g) for g in grid]))

    ds = "".join(inputs[1].split("\n"))
    n = len(grid)
    m = len(grid[0])

    s = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                s = (j, i)

    t = 0

    for d in ds:
        dir, _, slide = dirMap[d]
        np = getNextPos(grid, s, dir)

        if np:
            newGrid = copy.deepcopy(grid)
            if newGrid[np[1]][np[0]] != ".":
                newGrid = slide(grid, np)
            if newGrid[np[1]][np[0]] == ".":
                newGrid[np[1]][np[0]] = "@"
                newGrid[s[1]][s[0]] = "."
                grid = newGrid
                s = np
            # print("\n".join("".join(g) for g in grid))

    for i in range(n):
        print("".join(grid[i]))
        for j in range(m):
            if grid[i][j] == "[":
                t += i * 100 + j

    return t


print("-------- Day 15 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
