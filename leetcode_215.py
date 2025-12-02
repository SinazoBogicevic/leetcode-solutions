import heapq
from typing import List


def findKLargest(nums: List[int], k: int) -> int:

    # max heap solution
    # time: n + K long n
    # for i, val in enumerate(nums):
    #     nums[i] = -val

    # heapq.heapify(nums)

    # for _ in range(k - 1):
    #     heapq.heappop(nums)

    # return -heapq.heappop(nums)

    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)

    return min_heap[0]


if __name__ == "__main__":
    nums_list = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k_ = 4
    result = findKLargest(nums_list, k_)
    print(f"result: {result}")
