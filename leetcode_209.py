from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    l, min_length = 0, float("inf")
    running_sum = 0

    for r in range(len(nums)):
        running_sum += nums[r]

        while running_sum > target:
            window_size = (r - l) + 1
            min_length = min(min_length, window_size)

            running_sum -= nums[l]
            l += 1

    return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    target = 11
    nums = [1, 2, 3, 4, 5]
    result = minSubArrayLen(target, nums)
    print(f"Result: {result}")
