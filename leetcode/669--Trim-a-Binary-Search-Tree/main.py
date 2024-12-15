from typing import Optional 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None: return root
        left = self.trimBST(root.left, low, high)
        right = self.trimBST(root.right, low, high)
        if root.val <= high and root.val >= low:
            root.left = left
            root.right = right
        else:
            if left is not None:
                root = left
            else:
                root = right
        return root

        
