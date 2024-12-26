from typing import Optional

# Better Solution:
# 1. count the node depth then ignore nodes which has not enough depth as the subRoot
# 2. serialize the root tree into a string then compare with the sub root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootMatch = self.checkEqualTree(root, subRoot)
        if rootMatch: return True
        if not root: return False
        if self.isSubtree(root.left, subRoot): return True
        if self.isSubtree(root.right, subRoot): return True
        return False
    
    def checkEqualTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and root2:
            if root1.val == root2.val: 
                return self.checkEqualTree(root1.left, root2.left) and self.checkEqualTree(root1.right, root2.right)
            return False
        if root1 or root2: return False
        return True
