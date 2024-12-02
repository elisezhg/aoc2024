inputs_example = open("day02/day02_example.txt").read().split("\n")
inputs = open("day02/day02.txt").read().split("\n")


def part1(inputs):
    total = 0
    for levels in inputs:
        if isSafe(levels.split(" ")):
            total += 1

    return total


def part2(inputs):
    total = 0
    for levels in inputs:
        possibles = []

        for i in range(len(levels.split(" "))):
            newList = levels.split(" ")
            del newList[i]
            possibles.append(newList)

        for p in possibles:
            if isSafe(p):
                total += 1
                break

    return total


def isSafe(levels):
    direction = None
    last = None
    isValid = True

    for level in levels:
        if last is None:
            last = int(level)
            continue

        diff = int(level) - last
        curDir = 1 if diff > 0 else -1
        if not (abs(diff) >= 1 and abs(diff) <= 3) or (
            direction is not None and direction != curDir
        ):
            isValid = False
            break

        direction = curDir
        last = int(level)
    return isValid


print("-------- Day 02 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
