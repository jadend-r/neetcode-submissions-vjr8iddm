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
        nodez = {}
        if not head:
            return None

        
        copyHead = Node(head.val, head.next, head.random)
        nodez[head] = copyHead
        dummy = Node(0, copyHead)
        tail = copyHead

        curr = head.next
        while curr:
            # make copy and add to tail
            copy = Node(curr.val, curr.next, curr.random)
            tail.next = copy
            tail = tail.next
            # map old node -> new node
            nodez[curr] = copy
            curr = curr.next

        print(nodez)
        while head:
            if head.next:
                copyHead.next = nodez[head.next]
            if head.random:
                print(head.random)
                copyHead.random = nodez[head.random]
            copyHead = copyHead.next
            head = head.next

        return dummy.next

        

        
