from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda interval: interval[0])
    merged_intervals: List[List[int]] = []

    for start, end in intervals:

        if not merged_intervals or merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1] = [
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], end),
            ]

    return merged_intervals


# time complexity is nLogn because python's sort (and sorted )is a hybrid of Merge Sort and Insertion sort
