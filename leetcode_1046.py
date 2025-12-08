import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    # time complexity: O(nlogn)
    # space complexity: O(n)
    arr = []

    for num in stones:
        arr.append(-num)

    heapq.heapify(arr)

    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        result = first - second

        if result != 0:
            heapq.heappush(arr, result)  # O(nlogn)

    return arr[0] * -1 if len(arr) else 0


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    result_ = lastStoneWeight(stones)
    print(f"result: {result_}")
