def containsDuplicate(nums: list[int]) -> bool:
    hash_map: dict[int, int] = {}

    for index, num in enumerate(nums):
        if num in hash_map:
            return True
        hash_map[num] = index

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    result = containsDuplicate(nums)
    print(f"Result: {result}")
