from typing import List


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    index_map = {value: i for i, value in enumerate(nums1)}
    answer = [-1] * len(nums1)
    stack: List[int] = []

    # pylint: disable=C0200
    # for i in range(len(nums1)):
    #     print(f"i: {nums1[i]}")
    #     for j in range(nums2.index(nums1[i]) + 1, len(nums2)):

    #         if nums2[j] > nums1[i]:
    #             answer[i] = nums2[j]
    #             break

    for num in nums2:
        while stack and stack[-1] < num:
            stack_num = stack.pop()
            index = index_map[stack_num]
            answer[index] = num

        if num in index_map:
            stack.append(num)

    return answer


if __name__ == "__main__":
    nums1_ = [4, 1, 2]
    nums2_ = [1, 3, 4, 2]
    result = nextGreaterElement(nums1_, nums2_)
    print(f"result: {result}")
