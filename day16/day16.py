inputs_example = open("day16/day16_example.txt").read().split("\n")
inputs = open("day16/day16.txt").read().split("\n")

import heapq


def getNode(inputs, x, y):
    if 0 <= y < len(inputs) and 0 <= x < len(inputs[0]):
        return (x, y)
    else:
        return None


def part1(inputs):
    inputs = [list(i) for i in inputs]

    for i, r in enumerate(inputs):
        for j, c in enumerate(r):
            if c == "S":
                S = (j, i)
            elif c == "E":
                E = (j, i)

    visited = set()
    stack = [(0, S[0], S[1], None, None)]
    scores = []

    while stack:
        score, x, y, prevX, prevY = heapq.heappop(stack)

        if (x, y, prevX, prevY) in visited:
            continue
        elif scores and score >= min(scores):
            continue
        else:
            visited.add((x, y, prevX, prevY))

        if (x, y) == E:
            scores.append(score)
            continue

        possibleIdx = [
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
        ]

        possibleNodes = [getNode(inputs, *idx) for idx in possibleIdx]
        possibleNodes = [n for n in possibleNodes if n is not None]
        for node in possibleNodes:
            if inputs[node[1]][node[0]] != "#":
                rot = node[1] != prevY and node[0] != prevX
                heapq.heappush(
                    stack, (score + 1001 if rot else score + 1, node[0], node[1], x, y)
                )

    return min(scores)


def part2(inputs):
    inputs = [list(i) for i in inputs]

    for i, r in enumerate(inputs):
        for j, c in enumerate(r):
            if c == "S":
                S = (j, i)
            elif c == "E":
                E = (j, i)

    visitedScore = dict()
    seen = set()
    seen.add(S)
    stack = [(0, S[0], S[1], None, None, seen)]
    routes = []

    while stack:
        score, x, y, prevX, prevY, seen = heapq.heappop(stack)

        if (x, y, prevX, prevY) in visitedScore and visitedScore[
            (x, y, prevX, prevY)
        ] < score:
            continue
        else:
            visitedScore[(x, y, prevX, prevY)] = score

        if (x, y) == E:
            routes.append((score, seen))
            continue

        possibleIdx = [
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
        ]

        possibleNodes = [getNode(inputs, *idx) for idx in possibleIdx]
        possibleNodes = [n for n in possibleNodes if n is not None]
        for node in possibleNodes:
            if inputs[node[1]][node[0]] != "#":
                rot = node[1] != prevY and node[0] != prevX
                nscore = score + 1001 if rot else score + 1
                ns = seen.copy()
                ns.add(node)
                heapq.heappush(stack, (nscore, node[0], node[1], x, y, ns))

    bestScore = min([r[0] for r in routes])
    nodes = set()

    for score, seen in routes:
        if score == bestScore:
            for node in seen:
                nodes.add(node)

    # printGrid(inputs, nodes)

    return len(nodes)


def printGrid(grid, nodes):
    for i, r in enumerate(grid):
        res = ""
        for j, c in enumerate(r):
            if (j, i) in nodes:
                res += "O"
            else:
                res += inputs[i][j]
        print(res)


print("-------- Day 16 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")
print(f"\t{part2(inputs)}")
