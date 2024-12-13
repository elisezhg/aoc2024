inputs_example = open("day13/day13_example.txt").read().split("\n\n")
inputs = open("day13/day13.txt").read().split("\n\n")

from sympy import Eq, S, solve, symbols


def part1(inputs):

    total = 0

    for machine in inputs:
        btnA, btnB, prize = machine.split("\n")
        btnA = btnA.split(": ")[1].split(", ")
        btnA = [int(n[2:]) for n in btnA]

        btnB = btnB.split(": ")[1].split(", ")
        btnB = [int(n[2:]) for n in btnB]

        prize = prize.split(": ")[1].split(", ")
        prize = [int(n[2:]) for n in prize]

        eqs = []
        vars = symbols("A B")

        eqs.append(
            Eq(
                *map(
                    S,
                    (
                        f"{prize[0]}",
                        f"A * {btnA[0]} + B * {btnB[0]}",
                    ),
                )
            ),
        )

        eqs.append(
            Eq(
                *map(
                    S,
                    (
                        f"{prize[1]}",
                        f"A * {btnA[1]} + B * {btnB[1]}",
                    ),
                )
            ),
        )

        res = solve(eqs, vars)
        if res.values():
            a, b = res.values()
            if a // 1 != a or b // 1 != b:
                continue
            if int(a) <= 100 and int(b) <= 100:
                total += int(a) * 3 + int(b)

    return total


def part2(inputs):
    total = 0

    for machine in inputs:
        btnA, btnB, prize = machine.split("\n")
        btnA = btnA.split(": ")[1].split(", ")
        btnA = [int(n[2:]) for n in btnA]

        btnB = btnB.split(": ")[1].split(", ")
        btnB = [int(n[2:]) for n in btnB]

        prize = prize.split(": ")[1].split(", ")
        prize = [int(n[2:]) for n in prize]

        eqs = []
        vars = symbols("A B")

        eqs.append(
            Eq(
                *map(
                    S,
                    (
                        f"{prize[0]} + 10000000000000",
                        f"A * {btnA[0]} + B * {btnB[0]}",
                    ),
                )
            ),
        )

        eqs.append(
            Eq(
                *map(
                    S,
                    (
                        f"{prize[1]} + 10000000000000",
                        f"A * {btnA[1]} + B * {btnB[1]}",
                    ),
                )
            ),
        )

        res = solve(eqs, vars)
        if res.values():
            a, b = res.values()
            if a // 1 != a or b // 1 != b:
                continue
            total += int(a) * 3 + int(b)
    return total


print("-------- Day 13 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
