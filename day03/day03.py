inputs_example = open("day03/day03_example.txt").read()
inputs = open("day03/day03.txt").read()


def part1(inputs):
    total = 0
    i = 0

    while i < len(inputs):
        valid = False
        l, r = "", ""
        s = i

        commaFound = False

        # left
        if inputs[i:].startswith("mul("):
            s += 4
            while s < len(inputs):
                if inputs[s].isnumeric():
                    l += inputs[s]
                    s += 1
                elif inputs[s] == "," and l != "":
                    commaFound = True
                    s += 1
                    break
                else:
                    s += 1
                    break

        if not commaFound:
            i += 1
            continue

        # right
        while s < len(inputs):
            if inputs[s].isnumeric():
                r += inputs[s]
                s += 1
            elif inputs[s] == ")" and r != "":
                valid = True
                s += 1
                break
            else:
                s + 1
                break

        if valid:
            total += int(l) * int(r)
            i = s
        else:
            i += 1

    return total


def part2(inputs):
    enabled = True
    total = 0
    i = 0

    while i < len(inputs):
        valid = False
        l, r = "", ""
        s = i

        commaFound = False

        if inputs[i:].startswith("don't()"):
            enabled = False
        elif inputs[i:].startswith("do()"):
            enabled = True

        # left
        if inputs[i:].startswith("mul("):
            s += 4
            while s < len(inputs):
                if inputs[s].isnumeric():
                    l += inputs[s]
                    s += 1
                elif inputs[s] == "," and l != "":
                    commaFound = True
                    s += 1
                    break
                else:
                    s += 1
                    break

        if not commaFound:
            i += 1
            continue

        # right
        while s < len(inputs):
            if inputs[s].isnumeric():
                r += inputs[s]
                s += 1
            elif inputs[s] == ")" and r != "":
                valid = True
                s += 1
                break
            else:
                s + 1
                break

        if valid and enabled:
            total += int(l) * int(r)
            i = s
        else:
            i += 1

    return total


print("-------- Day 03 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
