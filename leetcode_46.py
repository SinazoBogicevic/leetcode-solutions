def permute(nums: list[int]) -> list[list[int]]:
    """Given an array nums of distinct integers, return all the possible permutations.
     You can return the answer in any order.

    Args:
        nums (list[int]): _description_

    Returns:
        list[list[int]]:
    """
    n = len(nums)
    # res, sol = list[list[int]], [int] type for res wrong because I'm initializing it with instead of typing it, correct: res: list[list[int]] = []
    res: list[list[int]] = []
    sol: list[int] = []

    def backtrack():

        if len(sol) == n:
            res.append(sol[:])  # this appends copy of sol
            return

        for x in nums:
            if x in sol:
                continue

            sol.append(x)
            backtrack()
            sol.pop()

    backtrack()
    return res


# Time: O(n!)
# Space: O(n)

# remember DFS (do it again tomorrow)
