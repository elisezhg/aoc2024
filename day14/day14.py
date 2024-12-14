inputs_example = open("day14/day14_example.txt").read().split("\n")
inputs = open("day14/day14.txt").read().split("\n")
import math


def part1(inputs, w, h):
    rs = []
    secs = 100
    for r in inputs:
        p, v = r.split(" ")
        p = [int(x) for x in p[2:].split(",")]
        v = [int(x) for x in v[2:].split(",")]

        x = p[0] + v[0] * secs
        x = x % w

        y = p[1] + v[1] * secs
        y = y % h

        rs.append((x, y))

    vert1 = math.floor(w / 2)
    vert2 = math.ceil(w / 2)
    hor1 = math.floor(h / 2)
    hor2 = math.ceil(h / 2)

    q1, q2, q3, q4 = 0, 0, 0, 0
    grid = [["." for i in range(w)] for j in range(h)]

    for x, y in rs:
        grid[y][x] = "X"
        if x < vert1 and y < hor1:
            q1 += 1
        elif x >= vert2 and y < hor1:
            q2 += 1
        elif x < vert1 and y >= hor2:
            q3 += 1
        elif x >= vert2 and y >= hor2:
            q4 += 1

    # print("\n".join(["".join(g) for g in grid]))

    return q1 * q2 * q3 * q4


def part2(inputs, w, h):
    for secs in range(10000):
        if secs % 1000 == 0:
            print(f"Iteration {secs}")

        rs = []
        valid = True

        for r in inputs:
            p, v = r.split(" ")
            p = [int(x) for x in p[2:].split(",")]
            v = [int(x) for x in v[2:].split(",")]

            x = p[0] + v[0] * secs
            x = x % w

            y = p[1] + v[1] * secs
            y = y % h

            # Ensure no overlap
            if (x, y) in rs:
                valid = False

            rs.append((x, y))

        if not valid:
            continue

        grid = [["." for i in range(w)] for j in range(h)]

        for x, y in rs:
            grid[y][x] = "X"

        print(f"------ {secs} ------")
        print("\n".join(["".join(g) for g in grid]))


print("-------- Day 14 --------")
print("Part 1:")
print(f"\t{part1(inputs_example, 11, 7)}")
print(f"\t{part1(inputs, 101, 103)}")
print("Part 2:")
print(f"\t{part2(inputs, 101, 103)}")
