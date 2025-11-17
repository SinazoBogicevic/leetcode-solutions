def move_zeroes(nums: list[int]) -> None:
    """
    This function moves all zeroes to the end of the list while maintaining the order of the non-zero elements.
    """
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1


if __name__ == "__main__":
    nums_list = [0, 1, 0, 3, 12]
    move_zeroes(nums_list)
    print(nums_list)
