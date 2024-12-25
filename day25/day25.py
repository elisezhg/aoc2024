inputs_example = open("day25/day25_example.txt").read().split("\n\n")
inputs = open("day25/day25.txt").read().split("\n\n")


def part1(inputs):
    inputs = [i.split() for i in inputs]
    locks = [
        i for i in inputs if list(set(i[0])) == ["#"] and list(set(i[-1])) == ["."]
    ]
    keys = [i for i in inputs if list(set(i[0])) == ["."] and list(set(i[-1])) == ["#"]]

    lockHeights = [convertToHeights(x) for x in locks]
    keyHeights = [convertToHeights(x) for x in keys]
    maxheight = len(locks[0]) - 1

    total = 0
    for lh in lockHeights:
        for kh in keyHeights:
            if not isOverlapping(lh, kh, maxheight):
                total += 1

    return total


def convertToHeights(grid):
    grid = [list(i) for i in grid]
    n = len(grid)
    m = len(grid[0])
    heights = []

    for x in range(m):
        h = -1
        for y in range(n):
            if grid[y][x] == "#":
                h += 1
        heights.append(h)

    return heights


def isOverlapping(heights1, heights2, maxH):
    for h1, h2 in zip(heights1, heights2):
        if h1 + h2 >= maxH:
            return True
    return False


print("-------- Day 25 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
