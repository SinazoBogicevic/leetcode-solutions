from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    total_sum = sum(nums[:k])
    max_avg = total_sum / k

    for i in range(k, len(nums)):
        left = i - k
        total_sum = total_sum - nums[left] + nums[i]
        curr_avg = total_sum / k

        max_avg = max(max_avg, curr_avg)

    return max_avg


if __name__ == "__main__":
    nums_ = [1, 12, -5, -6, 50, 3]
    k_ = 4
    result = findMaxAverage(nums_, k_)
    print(f"result: {result}")
