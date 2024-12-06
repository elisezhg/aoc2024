inputs_example = open("day06/day06_example.txt").read().split("\n")
inputs = open("day06/day06.txt").read().split("\n")


def getNextPos(grid, pos, dir):
    newX, newY = (pos[0] + dir[0], pos[1] + dir[1])

    if newX < 0 or newX >= len(grid[0]):
        return None

    if newY < 0 or newY >= len(grid):
        return None

    return newX, newY


def rot90(curDir):
    if curDir == (0, -1):
        return (1, 0)
    elif curDir == (1, 0):
        return (0, 1)
    elif curDir == (0, 1):
        return (-1, 0)
    elif curDir == (-1, 0):
        return (0, -1)
    else:
        print("wrong??")


def part1(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for i in inputs]

    s = (0, 0)
    for y in range(m - 1):
        for x in range(n - 1):
            if grid[y][x] == "^":
                s = (x, y)
                break

    visited[s[1]][s[0]] = True

    curDir = (0, -1)
    curPos = s

    while True:
        pos = getNextPos(grid, curPos, curDir)
        if not pos:
            break
        if grid[pos[1]][pos[0]] == "#":
            curDir = rot90(curDir)
        else:
            visited[pos[1]][pos[0]] = True
            curPos = pos

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

    s = (0, 0)
    for y in range(m - 1):
        for x in range(n - 1):
            if grid[y][x] == "^":
                s = (x, y)
                break

    blocked = 0

    for y in range(m):
        for x in range(n):
            alteredGrid = [i.copy() for i in grid]
            if alteredGrid[y][x] == ".":
                alteredGrid[y][x] = "#"

                visited = [[False] * m for i in inputs]
                visited[s[1]][s[0]] = True

                curDir = (0, -1)
                curPos = s

                while True:
                    pos = getNextPos(alteredGrid, curPos, curDir)
                    if not pos:
                        break

                    if alteredGrid[pos[1]][pos[0]] == "#":
                        curDir = rot90(curDir)
                    elif visited[pos[1]][pos[0]] == curDir:
                        blocked += 1
                        break
                    else:
                        visited[pos[1]][pos[0]] = curDir
                        curPos = pos

    return blocked


print("-------- Day 06 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
