from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]):
    if root is None: return
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invertTree(root) 
        return root   
