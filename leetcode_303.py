def sumRange(nums: list[int], left: int, right: int) -> int:
    sum_list: list[int] = []
    total = 0

    for num in nums:
        total += num
        sum_list.append(total)

    right_sum = sum_list[right]
    left_sum = sum_list[left - 1] if left > 0 else 0

    return right_sum - left_sum


if __name__ == "__main__":
    nums_ = [1, 2, 3, 4, 5]
    leftIndex = 0
    rightIndex = 2
    result = sumRange(nums_, leftIndex, rightIndex)
    print(f"Result: {result}")
