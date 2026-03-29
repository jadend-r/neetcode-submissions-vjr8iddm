# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        maxStack = []
        self.res = 0

        def dfs(curr):
            if not curr:
                return None

            maxStack.append(max(curr.val, maxStack[-1] if maxStack else curr.val))

            if curr.val >= maxStack[-1]:
                self.res += 1

            dfs(curr.left)
            dfs(curr.right)
            maxStack.pop()

        dfs(root)
        return self.res
