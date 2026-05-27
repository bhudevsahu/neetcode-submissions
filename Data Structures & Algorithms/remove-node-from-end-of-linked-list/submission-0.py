# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        index_to_remove = len(nodes) - n
        
        prev, curr = None, head
        for i in range(len(nodes)):
            if i == index_to_remove:
                if not prev:
                    head = curr.next
                    return head
                else:
                    prev.next = curr.next

            prev = curr
            curr = curr.next
        
        return head




        
        