from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # values in tree are unique
        if not len(inorder): # case when there is no left node
            return None 
        root_node = TreeNode()
        root_node.val = preorder.pop(0) # preorder has same len as inorder
        index = inorder.index(root_node.val)
        root_node.left = self.buildTree(preorder, inorder[:index]) 
        root_node.right = self.buildTree(preorder, inorder[index+1:])

        return root_node
