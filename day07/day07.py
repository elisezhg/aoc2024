inputs_example = open("day07/day07_example.txt").read().split("\n")
inputs = open("day07/day07.txt").read().split("\n")


def part1(inputs):
    total = 0

    for eq in inputs:
        res, nums = eq.split(": ")
        res = int(res)
        nums = [int(i) for i in nums.split(" ")]

        valid = is_possible(res, nums)

        if valid:
            total += res

    return total


def is_possible(res, nums):
    if len(nums) == 1:
        return nums[0] == res
    elif len(nums) == 2:
        [a, b] = nums
        return a * b == res or a + b == res
    else:
        cur, rest = nums[-1], nums[:-1]
        return is_possible(res / cur, rest) or is_possible(res - cur, rest)


def part2(inputs):
    total = 0

    for eq in inputs:
        res, nums = eq.split(": ")
        res = int(res)
        nums = [int(i) for i in nums.split(" ")]

        ps = [nums.pop(0)]
        while nums:
            val2 = nums.pop(0)
            nps = []
            while ps:
                val = ps.pop()
                nps.append(val + val2)
                nps.append(val * val2)
                nps.append(int(str(val) + str(val2)))
            ps = nps

        valid = False
        while ps:
            val = ps.pop()
            if val == res:
                valid = True
                break

        if valid:
            # print(eq, valid)
            total += res

    return total


print("-------- Day 07 --------")
print("Part 1:")
print(f"\t{part1(inputs_example)}")  # 3749
print(f"\t{part1(inputs)}")
print("Part 2:")
print(f"\t{part2(inputs_example)}")  # 11387
print(f"\t{part2(inputs)}")
