inputs_example = open("day23/day23_example.txt").read().split()
inputs = open("day23/day23.txt").read().split()

from collections import defaultdict


def getSortedKey(*c):
    return tuple(sorted([*c]))


# https://www.geeksforgeeks.org/maximal-clique-problem-recursive-solution/
def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph
        )
        X.add(v)


def part1(inputs):
    seen = defaultdict(set)
    lans = set()
    missing = defaultdict(set)

    for line in inputs:
        c1, c2 = line.split("-")
        key = getSortedKey(c1, c2)

        if key in missing:
            for c0 in missing[key]:
                lans.add(getSortedKey(c1, c2, c0))

        if seen[c1]:
            for c0 in seen[c1]:
                missing[getSortedKey(c0, c2)].add(c1)
        if seen[c2]:
            for c0 in seen[c2]:
                missing[getSortedKey(c0, c1)].add(c2)

        seen[c1].add(c2)
        seen[c2].add(c1)

    total = 0

    for c0, c1, c2 in lans:
        if c0[0] == "t" or c1[0] == "t" or c2[0] == "t":
            total += 1

    return total


def part2(inputs):
    edges = []
    nodes = set()

    for line in inputs:
        c1, c2 = line.split("-")
        edges.append(getSortedKey(c1, c2))
        nodes.add(c1)
        nodes.add(c2)

    # Create an adjacency list from the edges
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Convert set keys into sorted lists for consistent ordering
    graph = {key: set(graph[key]) for key in graph}

    cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))

    maxCliqueKeys = list(getSortedKey(*sorted(cliques, reverse=True, key=len)[0]))

    return ",".join(maxCliqueKeys)


print("-------- Day 23 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
