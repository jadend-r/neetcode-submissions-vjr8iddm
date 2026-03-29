# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dig(node):
            if not node:
                return 0
            left = dig(node.left)
            right = dig(node.right)
            return 1 + max(left, right)

        return dig(root)