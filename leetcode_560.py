from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    """
    This function counts the number of sub_arrays that sum to k.
    """
    count = 0
    curr_sum = 0

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         curr_sum = sum(nums[i : j + 1])
    #         print(f"curr_sum: {curr_sum}")
    #         if curr_sum == k:
    #             count += 1
    # This is a brute force solution, it's not efficient because it's O(n^2) time complexity.
    # We can use a hash map to store the cumulative sum and the number of times it appears.
    # Then we can use the hash map to check if the cumulative sum - k exists in the hash map.
    # If it does, we add the number of times it appears to the count.
    # This is a more efficient solution because it's O(n) time complexity.

    hash_map = {0: 1}

    for num in nums:
        curr_sum += num
        diff = curr_sum - k

        count += hash_map.get(diff, 0)
        hash_map[curr_sum] = hash_map.get(curr_sum, 0) + 1

    return count


if __name__ == "__main__":
    nums_list = [1, 2, 3]
    target_sum = 3
    RESULT = subarray_sum(nums_list, target_sum)
    print(f"Result: {RESULT}")
