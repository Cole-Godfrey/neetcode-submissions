"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldToCopy = {}
        cur = head
        # first pass - create copy nodes for the whole list (only the values)
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        # second pass - connect nodes (next + random)
        cur = head
        while cur:
            copy = oldToCopy[cur]
            if cur.next:
                copy.next = oldToCopy[cur.next]
            if cur.random:
                copy.random = oldToCopy[cur.random]

            cur = cur.next
        return oldToCopy[head]


        