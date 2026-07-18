# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal placing the elemns into an array
            #return the kth elem
        #O(n) time/space
        curr = root
        stack = []
        n = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right

        #root = [4,3,5,2,null], k = 4
        #self.res = [2, 3, 4, 5]
