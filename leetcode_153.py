from typing import List


def findMin(nums: List[int]) -> int:
    # tme complexity: O(n)
    # space complexity: O(n)

    # min_heap: List[int] = []

    # for num in nums:
    #     min_heap.append(num)

    # heapq.heapify(min_heap)

    # return min_heap[0]

    # more efficient solution
    # tme complexity: O(logn)
    # space complexity: O(1)
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    return nums[l]


if __name__ == "__main__":

    nums_ = [3, 4, 5, 1, 2]
    RESULT = findMin(nums_)
    print(f"result: {RESULT}")
