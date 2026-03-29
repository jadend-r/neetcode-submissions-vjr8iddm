# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next: 
            slow = slow.next   #shift slow by 1
            fast = fast.next.next # shift fast by 2

        # reverse second hald
        second = slow.next
        prev = slow.next = None 
        while second:
            n = second.next
            second.next = prev
            prev = second
            second = n

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
