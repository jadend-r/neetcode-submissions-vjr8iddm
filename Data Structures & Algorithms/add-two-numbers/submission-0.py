# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        place = 1
        curr = l1
        while curr:
            sum += place * curr.val
            place *= 10
            curr = curr.next

        place = 1
        curr = l2
        while curr:
            sum += place * curr.val
            place *= 10
            curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        for num in str(sum)[::-1]:
            n = ListNode(int(num))
            tail.next = n
            tail = tail.next

        return dummy.next