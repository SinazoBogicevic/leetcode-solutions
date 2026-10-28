from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    # recursive solution
    # time complexity: O(n)
    # space complexity: O(n)
    # if not root:
    #     return 0

    # left = maxDepth(root.left)
    # right = maxDepth(root.right)

    # return 1 + max(left, right)

    if not root:
        return 0

    total_max_depth = 0
    stack = [(root, 1)]

    while stack:
        node, depth = stack.pop()
        total_max_depth = max(total_max_depth, depth)

        if node.left:
            stack.append((node.left, 1))
            total_max_depth = max(total_max_depth, 1)

        if node.right:
            stack.append((node.right, 1))
            total_max_depth = max(total_max_depth, 1)

    return total_max_depth


if __name__ == "__main__":
    root_ = TreeNode(1)
    root_.left = TreeNode(2)
    root_.right = TreeNode(3)
    root_.left.left = TreeNode(4)
    root_.left.right = TreeNode(5)

    result_ = maxDepth(root_)
    print(f"Result: {result_}")
