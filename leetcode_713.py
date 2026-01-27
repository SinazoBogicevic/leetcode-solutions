from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    count, l, prod = 0, 0, 1

    # pylint: disable=C0200
    # Time complexity O(n2) space: O(1)
    # for i in range(len(nums)):
    #     prod = 1
    #     for j in range(i, len(nums)):
    #         prod = prod * nums[j]

    #         if prod < k:
    #             count += 1

    # edge case
    # If k is 0 or 1, no product of positive integers can be < k
    # if k <= 1:
    #     return 0

    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k and l <= r:
            prod = prod // nums[l]
            l += 1

        count += (r - l) + 1

    return count


if __name__ == "__main__":
    nums_ = [10, 5, 2, 6]
    k_ = 100
    result = numSubarrayProductLessThanK(nums_, k_)
    print(f"result: {result}")
