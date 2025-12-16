from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # time complexity: O(nLogn)
    # space complexity: O(n)
    # not the optimal solution
    # merged_intervals: List[List[int]] = []

    # intervals.append(newInterval)

    # intervals.sort(key=lambda interval: interval[0])

    # for start, end in intervals:

    #     if not merged_intervals or merged_intervals[-1][1] < start:
    #         merged_intervals.append([start, end])
    #     else:

    #         merged_intervals[-1] = [
    #             merged_intervals[-1][0],
    #             max(merged_intervals[-1][1], end),
    #         ]

    # time complexity: O(n)
    # space complexity: O(n)
    merged_intervals: List[List[int]] = []

    l, r, target = 0, len(intervals) - 1, newInterval[0]

    while l <= r:
        m = (l + r) // 2

        if intervals[m][0] < target:
            l = m + 1
        else:
            r = m - 1

    intervals.insert(l, newInterval)

    for start, end in intervals:
        if not merged_intervals or merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1] = [
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], end),
            ]

    return merged_intervals


if __name__ == "__main__":
    intervals_list = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newIntervals_ = [4, 8]
    result = insert(intervals_list, newIntervals_)
    print(f"Result: {result}")
