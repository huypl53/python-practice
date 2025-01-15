# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head: return head

        reversed_node = reversed_head = last_reverse = pre_last_reverse = None
        # reversed_head = None
        # node = None
        count = 0
        # last_reverse = None
        # pre_last_reverse = None
        while head:
            head_next = head.next
            head.next = reversed_node
            reversed_node = head
            # save returned head
            if count == k:
                reversed_head = reversed_node

            if count % k == 0:
                pre_last_reverse = last_reverse
                last_reverse = head
            if count % k == k - 1:
                if pre_last_reverse: pre_last_reverse.next = head
            count += 1
            head = head_next

        return reversed_head
