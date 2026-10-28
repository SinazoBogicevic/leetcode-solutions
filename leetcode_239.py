from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    This function returns the maximum sliding window of size k in the list nums.
    """
    result: List[int] = []

    # time complexity: O(n*k)
    # space complexity: O(n)

    # pylint: disable=C0200
    for i in range(len(nums) - k + 1):
        max_num = nums[i]
        for j in range(i + 1, i + k):
            max_num = max(max_num, nums[j])

        result.append(max_num)

    return result


if __name__ == "__main__":
    NUMS = [1, 3, -1, -3, 5, 3, 6, 7]
    K = 3
    result_ = max_sliding_window(NUMS, K)
    print(f"Result: {result_}")
