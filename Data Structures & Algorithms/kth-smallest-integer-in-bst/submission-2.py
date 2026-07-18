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
        self.res = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.res.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.res[k - 1]

        #root = [4,3,5,2,null], k = 4
        #self.res = [2, 3, 4, 5]
