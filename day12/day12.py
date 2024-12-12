inputs_example = open("day12/day12_example.txt").read().split("\n")
inputs = open("day12/day12.txt").read().split("\n")


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
    total = 0

    visited = [[False] * m for i in inputs]
    grps = []

    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                continue

            currGrp = grid[y][x]
            currGrpPts = set()
            currGrpPts.add((x, y))

            stack = [(x, y)]

            while stack:
                curPos = stack.pop()
                nx, ny = curPos

                if grid[ny][nx] != currGrp or visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                currGrpPts.add(curPos)

                for d in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                    pos = getNextPos(grid, curPos, d)
                    if pos:
                        stack.append(pos)

            grps.append(currGrpPts)

    for g in grps:

        p = 0
        for x, y in g:
            currGrp = grid[y][x]
            for d in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                pos = getNextPos(grid, (x, y), d)
                if not pos or grid[pos[1]][pos[0]] != currGrp:
                    p += 1

        # print("a", len(g), "p", p)
        total += len(g) * p

    return total


def part2(inputs):
    grid = [list(i) for i in inputs]
    n = len(grid)
    m = len(grid[0])
    total = 0

    visited = [[False] * m for i in inputs]
    grps = []

    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                continue

            currGrp = grid[y][x]
            currGrpPts = set()
            currGrpPts.add((x, y))

            stack = [(x, y)]

            while stack:
                curPos = stack.pop()
                nx, ny = curPos

                if grid[ny][nx] != currGrp or visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                currGrpPts.add(curPos)

                for d in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                    pos = getNextPos(grid, curPos, d)
                    if pos:
                        stack.append(pos)

            grps.append(currGrpPts)

    for g in grps:

        corners = 0
        for x, y in g:
            currGrp = grid[y][x]
            for d1, d2, d3 in [
                ((1, 0), (0, 1), (1, 1)),
                ((1, 0), (0, -1), (1, -1)),
                ((-1, 0), (0, 1), (-1, 1)),
                ((-1, 0), (0, -1), (-1, -1)),
            ]:
                pos1 = getNextPos(grid, (x, y), d1)
                pos2 = getNextPos(grid, (x, y), d2)
                pos3 = getNextPos(grid, (x, y), d3)

                if pos1 == pos2 == None:
                    corners += 1
                elif (pos1 is None and grid[pos2[1]][pos2[0]] is not currGrp) or (
                    pos2 is None and grid[pos1[1]][pos1[0]] is not currGrp
                ):
                    corners += 1
                elif (
                    pos1
                    and pos2
                    and grid[pos2[1]][pos2[0]] == grid[pos1[1]][pos1[0]]
                    and grid[pos3[1]][pos3[0]] != currGrp
                ):
                    corners += 1
                elif (
                    pos1
                    and pos2
                    and grid[pos2[1]][pos2[0]] != currGrp
                    and grid[pos1[1]][pos1[0]] != currGrp
                ):
                    corners += 1

        # print(currGrp, len(g) * corners, "a:", len(g), "c:", corners)
        total += len(g) * corners

    return total


print("-------- Day 12 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
