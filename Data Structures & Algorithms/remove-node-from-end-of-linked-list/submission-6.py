# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        dummy = prev
        fast = head

        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            prev = prev.next
            fast = fast.next

        prev.next = prev.next.next

        return dummy.next
