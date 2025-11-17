def runningSum(nums: list[int]) -> list[int]:
    total = 0
    running_sum: list[int] = []

    for num in nums:
        total += num
        running_sum.append(total)

    return running_sum


if __name__ == "__main__":
    nums_ = [1, 2, 3, 4]
    result = runningSum(nums_)
    print(f"Result: {result}")
