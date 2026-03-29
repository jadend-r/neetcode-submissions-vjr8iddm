# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swap(self, node):
        if node == None:
            return
        self.swap(node.left)
        self.swap(node.right)
        r = node.right
        node.right = node.left
        node.left = r
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)
        return root