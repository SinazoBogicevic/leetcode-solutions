from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
    """
    Given the root of a binary tree, return the inorder traversal of its nodes' values.

    Args:
        root (TreeNode): _description_

    Returns:
        List[int]: _description_
    """

    # recursive solution
    # time: O(n)
    # space: O(n)

    # res = []

    # def inorder(root):
    #     if not root:
    #         return
    #     inorder(root.left)
    #     res.append(root.val)
    #     inorder(root.right)

    # inorder(root)
    # return res

    # iterative solution
    # time O(n)
    # space: O(n) balanced tree would be O(logN)
    result: List[int] = []
    stack: List[TreeNode] = []
    curr: TreeNode | None = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


if __name__ == "__main__":
    root_ = TreeNode(1)
    root_.right = TreeNode(2)
    root_.right.left = TreeNode(3)

    result_ = inorder_traversal(root_)
    print(result_)
