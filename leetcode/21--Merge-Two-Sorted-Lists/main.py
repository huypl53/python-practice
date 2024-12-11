# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val > list2.val:
            node = list2
            list2 = list2.next
        else:
            node = list1
            list1 = list1.next

        head = node
        while True:
            print(f"{head} | {node.val} | { node} | { list1} | {list2 }")
            if list1 is None:
                node.next = list2
                return head
            if list2 is None:
                node.next = list1
                return head
            if list1.val > list2.val:
                node.next = list2
                node = list2
                list2 = list2.next
            else:
                node.next = list1
                node = list1
                list1 = list1.next


if __name__ == "__main__":
    list1 = [ListNode(v) for v in [1, 2, 4]]
    list2 = [ListNode(v) for v in [1, 3, 4]]
    for i in range(2):
        list1[i].next = list1[i + 1]
        list2[i].next = list2[i + 1]

    print("Before merged")
    print(list1[0])
    print(list2[0])

    print("After merged")
    s = Solution()
    merged = s.mergeTwoLists(list1[0], list2[0])
    print(merged)
