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
        oldToCopy = {None : None}

        curr = head
        while curr:
            # make copy and add to tail
            copy = Node(curr.val)
            # map old node -> new node
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

        

        
