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
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        l1 = head
        l2 = self.reverseList(s.next)

        while l1 != s:
            nxt1 = l1.next
            nxt2 = l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2
        
        l1.next = l2
        

