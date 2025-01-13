from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # number 0
        if l1.val == 0 and l1.next is None:
            return l2
        if l2.val == 0 and l2.next is None:
            return l1
        sum_node = ListNode()
        sum_list = sum_node
        sum_pre = 0
        while not (l1 is None and l2 is None):
            # print(l1 and l1.val, l2 and l2.val)
            if l1 is None:
                # sum_node
                if sum_pre == 0:
                    sum_node.next = l2
                    break
                else:
                    v = l2.val + sum_pre
                    l2.val = v % 10
                    sum_pre = v // 10
                    sum_node.next = l2
                    sum_node = l2
                l2 = l2.next
                continue
            if l2 is None:
                if sum_pre == 0:
                    sum_node.next = l1
                    break
                else:
                    v = l1.val + sum_pre
                    l1.val = v % 10
                    sum_pre = v // 10
                    sum_node.next = l1
                    sum_node = l1
                l1 = l1.next
                continue

            node = ListNode()
            v = l1.val + l2.val + sum_pre

            node.val = v % 10
            sum_pre = v // 10
            sum_node.next = node
            sum_node = node
            
            l1 = l1.next
            l2 = l2.next
        if sum_pre > 0:
            node = ListNode()
            node.val = sum_pre
            sum_node.next = node
        return sum_list.next
