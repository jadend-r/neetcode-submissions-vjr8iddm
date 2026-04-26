# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, prev):
            if not node:
                return 0
            
            maxV = max(prev, node.val)
            res = 1 if node.val >= maxV else 0

            left = dfs(node.left, maxV)
            right = dfs(node.right, maxV)
            return res + left + right

        return dfs(root, root.val)