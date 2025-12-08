import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # time complexity:  O(n)
        # space complexity: O(k)

        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # time complexity: O (logk)
        # space complexity: O(k)
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
