# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def dfs(curr1, curr2):
            if not curr1 and not curr2:
                return None
            if not curr1 or not curr2:
                self.same = False
                return None
            dfs(curr1.left, curr2.left)
            dfs(curr1.right, curr2.right)
            if curr1.val != curr2.val:
                self.same = False

        dfs(p, q)
        return self.same