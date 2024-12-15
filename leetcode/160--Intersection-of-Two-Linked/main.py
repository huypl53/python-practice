from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: Optional[ ListNode ], headB: Optional[ListNode]) -> Optional[ListNode]:
        stackA = []
        stackB = []
        while True:

            if not headA and not headB:
                break
                

            if headA: 
                stackA.append(headA)
                headA = headA.next

            if headB: 
                stackB.append(headB)
                headB = headB.next

        i = len(stackA) - 1 
        j = len(stackB) - 1 
        found = None
        while i >= 0 and j >= 0:
            if stackA[i] != stackB[j]:
                return found
            else:
                found = stackA[i]
            
            i -= 1
            j -= 1
        return found
