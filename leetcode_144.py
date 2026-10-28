# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Given the root of a binary tree, return the preorder traversal of its nodes' values.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.

    Returns:
        List[int]: The preorder traversal of the binary tree.
    """
    # iterative solution
    # time: O(n)
    # space: O(n)

    curr: TreeNode | None = root
    stack: List[TreeNode] = []
    result: List[int] = []

    while curr or stack:
        if curr:
            result.append(curr.val)
            stack.append(curr.right)
            curr = curr.left

        else:
            curr = stack.pop()

    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    res = preorderTraversal(root)
    print(res)
