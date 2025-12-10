from typing import List


def search(nums: List[int], target: int) -> int:
    # time complexity: O(log(n))
    # space complexity: 0(1)
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    min_index = l

    if min_index == 0:
        l, r = 0, len(nums) - 1
    elif target >= nums[0] and target <= nums[min_index - 1]:
        l, r = 0, min_index - 1
    else:
        l, r = min_index, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1

    return -1


if __name__ == "__main__":

    nums_ = [4, 5, 6, 7, 0, 1, 2]
    target_ = 0
    RESULT = search(nums_, target_)
    print(f"result: {RESULT}")
