inputs_example = open("day04/day04_example.txt").read().split()
inputs = open("day04/day04.txt").read().split()


def part1(inputs):
    m, n = len(inputs), len(inputs[0])

    occ = 0

    # horizontally
    for y in range(m):
        for x in range(n - 3):
            if inputs[y][x : x + 4] == "XMAS":
                occ += 1

            if inputs[y][x : x + 4] == "SAMX":
                occ += 1

    # vertically
    for y in range(m - 3):
        for x in range(n):
            if (
                inputs[y][x] + inputs[y + 1][x] + inputs[y + 2][x] + inputs[y + 3][x]
                == "XMAS"
            ):
                occ += 1

            if (
                inputs[y][x] + inputs[y + 1][x] + inputs[y + 2][x] + inputs[y + 3][x]
                == "SAMX"
            ):
                occ += 1

    # diagonally
    for y in range(m - 3):
        for x in range(n - 3):
            if (
                inputs[y][x]
                + inputs[y + 1][x + 1]
                + inputs[y + 2][x + 2]
                + inputs[y + 3][x + 3]
                == "XMAS"
            ):
                occ += 1

            if (
                inputs[y][x]
                + inputs[y + 1][x + 1]
                + inputs[y + 2][x + 2]
                + inputs[y + 3][x + 3]
                == "SAMX"
            ):
                occ += 1

            if (
                inputs[y][x + 3]
                + inputs[y + 1][x + 2]
                + inputs[y + 2][x + 1]
                + inputs[y + 3][x]
                == "XMAS"
            ):
                occ += 1

            if (
                inputs[y][x + 3]
                + inputs[y + 1][x + 2]
                + inputs[y + 2][x + 1]
                + inputs[y + 3][x]
                == "SAMX"
            ):
                occ += 1

    return occ


def part2(inputs):
    m, n = len(inputs), len(inputs[0])

    occ = 0

    for y in range(m - 2):
        for x in range(n - 2):
            a = inputs[y][x] + inputs[y + 1][x + 1] + inputs[y + 2][x + 2]
            b = inputs[y + 2][x] + inputs[y + 1][x + 1] + inputs[y][x + 2]
            if (a == "MAS" or a == "SAM") and (b == "SAM" or b == "MAS"):
                occ += 1

    return occ


print("-------- Day 04 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
