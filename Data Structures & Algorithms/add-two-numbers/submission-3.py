# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        carry = 0
        while l1 or l2:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            summ = v1 + v2 + carry
            digit = summ % 10 
            carry = summ // 10
            node = ListNode(digit)
            tail.next = node
            tail = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            node = ListNode(carry)
            tail.next = node

        return dummy.next