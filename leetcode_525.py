from typing import List


def find_max_length(nums: List[int]) -> int:
    """
    This function finds the maximum length of a contiguous subarray with an equal number of 0s and 1s.
    """
    prefix_sum = 0
    max_length = 0
    hash_map = {0: -1}

    for i, n in enumerate(nums):
        prefix_sum += n if n else prefix_sum - 1

        if prefix_sum in hash_map:
            max_length = max(max_length, i - hash_map[prefix_sum])

        else:
            hash_map[prefix_sum] = i

    return max_length


if __name__ == "__main__":
    nums_list = [0, 1, 0]
    RESULT = find_max_length(nums_list)
    print(f"Result: {RESULT}")
