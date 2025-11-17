from typing import List


def findDuplicate(nums: List[int]) -> int:

    slow, fast = 0, 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

        slow2 = 0

    while True:
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2:
            return slow


if __name__ == "__main__":
    nums_list = [1, 3, 4, 2, 2]
    result = findDuplicate(nums_list)
    print(f"Result: {result}")
