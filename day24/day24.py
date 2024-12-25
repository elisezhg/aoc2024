inputs_example = open("day24/day24_example.txt").read().split("\n\n")
inputs = open("day24/day24.txt").read().split("\n\n")


def part1(inputs, wires=None, connections=None):
    if not wires and not connections:
        wires, connections = inputs
        wires = [w.split(": ") for w in wires.split("\n")]
        wires = {w[0]: int(w[1]) for w in wires}
        connections = [c.split() for c in connections.split("\n")]

    hasChanged = True
    while hasChanged:
        oldLen = len(wires)

        for c in connections:
            w1, g, w2, _, o = c

            if w1 not in wires or w2 not in wires:
                continue

            if g == "AND":
                wires[o] = wires[w1] and wires[w2]
            elif g == "OR":
                wires[o] = wires[w1] or wires[w2]
            elif g == "XOR":
                wires[o] = int(wires[w1] != wires[w2])

        hasChanged = len(wires) != oldLen

    total = ""
    for k, v in sorted(wires.items(), reverse=True):
        if k.startswith("z"):
            total += str(v)

    return int(total, 2)


# See https://www.reddit.com/r/adventofcode/comments/1hla5ql/2024_day_24_part_2_a_guide_on_the_idea_behind_the/
def part2(inputs):
    wires, connections = inputs
    wires = [w.split(": ") for w in wires.split("\n")]
    wires = {w[0]: int(w[1]) for w in wires}
    connections = [c.split() for c in connections.split("\n")]

    lastZ = sorted([o for _, _, _, _, o in connections if o[0] == "z"], reverse=True)[0]

    susWires = set()

    for c in connections:
        w1, g, w2, _, o = c

        # If the output of a gate is z,
        # then the operation has to be XOR unless it is the last bit
        if o != lastZ and o[0] == "z" and g != "XOR":
            susWires.add(o)

        # If the output of a gate is not z and the inputs are not x, y
        # then it has to be AND / OR, but not XOR
        elif o[0] != "z" and w1[0] not in "xy" and w2[0] not in "xy" and g == "XOR":
            susWires.add(o)

        # The two following rules don't apply for the gates with input x00, y00
        elif w1[1:] == w2[1:] == "00":
            continue

        # If you have a XOR gate with inputs x, y,
        # there must be another XOR gate with this gate as an input
        elif (
            g == "XOR"
            and w1[0] in "xy"
            and w2[0] in "xy"
            and not searchGate(connections, o, "XOR")
        ):
            susWires.add(o)

        # If you have an AND-gate with inputs x, y,
        # there must be an OR-gate with this gate as an input
        elif (
            g == "AND"
            and w1[0] in "xy"
            and w2[0] in "xy"
            and not searchGate(connections, o, "OR")
        ):
            susWires.add(o)

    return ",".join(sorted(susWires))


def searchGate(connections, input, gate):
    for w1, g, w2, _, _ in connections:
        if g == gate and (w1 == input or w2 == input):
            return True

    return False


print("-------- Day 24 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
# print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
