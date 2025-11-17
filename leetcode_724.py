def pivotIndex(nums: list[int]) -> int:

    left_sum = 0
    total = sum(nums)

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]

        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1

    #     left_sum = 0

    #     left_sum = 0

    #         for i in range(len(nums)):
    #             right_sum = sum(nums[i+1:])
    #             if right_sum == left_sum:
    #                 return i
    #             left_sum += nums[i]

    #         return -1

    # This solution is not optimal, O(n²):  right_sum calculation is being done on every loop this involves making an array then adding the elements within that array, we're doing a lot of repeat work:
    # i = 0: sum = i0
    # i = 1 -> sum = i0 + i1
    # i = 2 -> sum =i0 + i1 + i2
    # Notice how we're repeating steps; this isn't efficient

    # That's why the most efficient solution involves us first compting the total outside of the loop.


if __name__ == "__main__":
    nums_ = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums_))
