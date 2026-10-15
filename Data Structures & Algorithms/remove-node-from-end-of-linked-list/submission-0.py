# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            # reverse arrow
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse list
        head = self.reverseList(head)
        # if we are removing first one, just move head
        if n == 1:
            head = head.next
        else:
            # move to node to be removed
            prev = head # node before one to be removed
            while n > 2:
                prev = prev.next
                n -= 1
            # remove it
            prev.next = prev.next.next

        # reverse list back to original
        head = self.reverseList(head)
        return head