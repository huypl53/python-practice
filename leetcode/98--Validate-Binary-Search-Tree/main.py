from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
        max_num: Optional[int] = float("inf"),
        min_num: Optional[int] = float("-inf"),
    ) -> bool:
        print(root.val if root else "Nope", max_num, min_num)

        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None:
            if root.left.val >= root.val or root.left.val <= min_num:
                return False
        if root.right is not None:
            if root.right.val <= root.val or root.right.val >= max_num:
                return False

        return self.isValidBST(root.left, root.val, min_num) and self.isValidBST(
            root.right, max_num, root.val
        )
