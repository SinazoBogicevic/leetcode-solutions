from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = set()

    # time complexity: O(n^3)
    # space complexity: O(m) where m is the number of triplets
    # pylint: disable=C0200
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return [list(t) for t in result]


if __name__ == "__main__":
    nums_ = [-1, 0, 1, 2, -1, -4]
    result_ = threeSum(nums_)
    print(f"Result: {result_}")
