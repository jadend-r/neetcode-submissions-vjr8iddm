# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #dummy node as head
        #counter -- reverse nodes in k group and attach to the tail
        dummy  = ListNode()
        tail = dummy

        idx = 0
        #try to reverse k nodes
        while head:
            #first walk k steps ahead to make sure we have k nodes
            curr = head
            for i in range(k):
                if not curr:
                    tail.next = head
                    return dummy.next
                curr = curr.next

            prev = None
            curr = head
            for i in range(k):
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
            tail.next = prev
            tail = head
            head = curr
        return dummy.next
        