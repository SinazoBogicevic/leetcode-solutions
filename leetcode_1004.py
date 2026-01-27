from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    l, num_zeros, max_len = 0, 0, 0
    n = len(nums)

    for r in range(n):
        if nums[r] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1

        w = (r - l) + 1
        max_len = max(max_len, w)

    return max_len


if __name__ == "__main__":
    nums_ = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k_ = 2
    result = longestOnes(nums_, k_)
    print(f"{result}")
