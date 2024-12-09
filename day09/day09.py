inputs_example = open("day09/day09_example.txt").read()
inputs = open("day09/day09.txt").read()


def checksum(val):
    total = 0
    for i, num in enumerate(val):
        if num and num != ".":
            total += i * int(num)
    return total


def part1(inputs):
    inputs = list(inputs)
    rep = []

    for i, n in enumerate(inputs):
        if i % 2 == 0:
            for _ in range(int(n)):
                rep.append(str((i + 1) // 2))
        else:
            for _ in range(int(n)):
                rep.append(".")

    # move left

    l, r = 0, len(rep) - 1

    while l < r:
        while rep[l] != "." and l < r:
            l += 1
        while rep[r] == "." and l < r:
            r -= 1

        if l < r:
            rep[l], rep[r] = rep[r], rep[l]

    return checksum(rep)


def part2(inputs):
    inputs = list(inputs)
    files = []
    spaces = []
    pos = 0

    for i, n in enumerate(inputs):
        if i % 2 == 0:
            files.append((pos, int(n)))
        else:
            spaces.append((pos, int(n)))
        pos += int(n)

    for fi in range(len(files) - 1, -1, -1):
        fp, size = files[fi]

        for si, (sp, space) in enumerate(spaces):
            if space >= size:
                files[fi] = (sp, size)
                spaces[si] = (sp + size, space - size)
                break

            if sp >= fp:
                break

    return checksum2(files)


def checksum2(files):
    total = 0
    for id, (pos, size) in enumerate(files):
        fTotal = 0
        for i in range(pos, pos + size):
            fTotal += id * i
        total += fTotal

    return total


print("-------- Day 09 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")  # 1928
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
