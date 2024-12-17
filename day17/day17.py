inputs_example = open("day17/day17_example.txt").read().split("\n\n")
inputs = open("day17/day17.txt").read().split("\n\n")

import math
from collections import defaultdict


def getCombo(ra, rb, rc, i):
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: ra,
        5: rb,
        6: rc,
    }
    return combo[i]


def compute(inputs, raOverride=None, asProgram=False):
    [rs, ins] = inputs
    rs = rs.split("\n")
    rs = list(map(int, [r.split(": ")[1] for r in rs]))
    [ra, rb, rc] = rs
    ins = list(map(int, ins.split(": ")[1].split(",")))
    outputs = []
    if raOverride:
        ra = raOverride

    i = 0
    while i < len(ins):
        opcode, operand = ins[i], ins[i + 1]
        # print(opcode, operand)

        if opcode == 0:
            ra = math.floor(ra / (2 ** getCombo(ra, rb, rc, operand)))
        elif opcode == 1:
            rb ^= operand
        elif opcode == 2:
            rb = getCombo(ra, rb, rc, operand) % 8
        elif opcode == 3:
            if ra != 0:
                i = operand * 2
                continue
        elif opcode == 4:
            rb ^= rc
        elif opcode == 5:
            outputs.append(getCombo(ra, rb, rc, operand) % 8)
        elif opcode == 6:
            rb = math.floor(ra / (2 ** getCombo(ra, rb, rc, operand)))
        elif opcode == 7:
            rc = math.floor(ra / (2 ** getCombo(ra, rb, rc, operand)))

        i += 2

    # print(ra, rb, rc)
    outputs = list(map(str, outputs))
    return ",".join(outputs) if not asProgram else "".join(outputs[::-1])


def part1(inputs):
    return compute(inputs)


def part2(inputs):
    ins = inputs[1].split(": ")[1].split(",")
    insStr = "".join(ins[::-1])
    n = len(ins)

    def bin_search_len(s, e, goal):
        if s > e:
            return False
        mid = (e + s) // 2
        res = len(compute(inputs, mid, True))
        if res == goal:
            return mid
        elif res > goal:
            return bin_search_len(s, mid - 1, goal)
        else:
            return bin_search_len(mid + 1, e, goal)

    start = bin_search_len(0, 1000000000000000, n - 1)
    end = bin_search_len(0, 1000000000000000, n + 1)

    def find_delta(digit, start, end, skip):
        prevVal, prevI = None, None
        for i in range(start, end, skip):
            if compute(inputs, i, True)[:digit] != prevVal:
                prevVal = compute(inputs, i, True)[:digit]
                if prevI:
                    return i - prevI
                prevI = i

    seen = set()

    def find_digit(digit, start, end, delta):
        candidates = set()
        for i in range(start, end, delta):
            if (i, digit) in seen:
                continue
            seen.add((i, digit))
            if compute(inputs, i, True)[: digit + 1] == insStr[: digit + 1]:
                candidates.add(i)
        return list(candidates)

    deltas = {}
    skips = {
        0: 10000000000,
        1: 1000000000,
        2: 100000000,
        3: 10000000,
        4: 1000000,
        5: 100000,
        6: 100000,
        7: 100000,
        8: 10000,
        9: 10,
    }

    for d in range(len(insStr)):
        skip = skips[d] if d in skips else 1
        deltas[d] = find_delta(d + 1, start, end, skip)
        # print(f"delta {deltas[d]} for digit {d}")

    candidates = defaultdict(list)
    candidates[0] = find_digit(0, start, end, deltas[0])

    for d in range(1, len(insStr)):
        for c in candidates[d - 1]:
            prevDelta = deltas[d - 1]
            delta = deltas[d]
            newCandidates = set(
                candidates[d] + find_digit(d, c - prevDelta, c + prevDelta, delta)
            )
            candidates[d] = list(newCandidates)
            candidates[d].sort()
        print(f"found {len(candidates[d])} candidates for digit {d}")
        print(candidates[d][0], compute(inputs, candidates[d][0], True))

    return candidates[len(insStr) - 1][0]


print("-------- Day 17 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
# print(f"\t{part2(inputs_example)}")  # 117440
print(f"\t{part2(inputs)}")
