# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.maxDepth(root)
        return self.res

    def maxDepth(self, node):
            if not node:
                return 0
            left = self.maxDepth(node.left)
            right = self.maxDepth(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)