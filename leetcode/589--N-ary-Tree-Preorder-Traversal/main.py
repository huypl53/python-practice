from typing import List, Optional, Union
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Union['Node',None]) -> List[int]:
        if root is None:
            return []
        bucket = [root]

        result = []
        while len(bucket) > 0:
            node = bucket.pop(0)
            result.append(node.val)

            if node.children is not None:
                bucket = node.children + bucket
        return result
