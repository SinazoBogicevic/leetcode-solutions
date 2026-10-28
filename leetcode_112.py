from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

    def dfs(node: Optional[TreeNode], running_sum: int) -> bool:

        if not node:
            return False

        running_sum += node.val

        if not node.left and not node.right:
            return running_sum == targetSum

        return dfs(node.left, running_sum) or dfs(node.right, running_sum)

    return dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(hasPathSum(root, 22))
