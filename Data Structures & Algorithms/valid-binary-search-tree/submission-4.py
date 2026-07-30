# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #brute force O(N^2), for every node, check entire subtree < node.val, check entire right subtree > node.val

        #optimize to o(n) by passing down in our dfs the range values for that subtree
        #root is allowed to be -inf to pos inf
            #left subtree, our max val becomes the root value
            #right subtree, min val becomes the root value
        
        #O(h) space for recursion stack h = height of binary tree balanced tree roughly log n
        #O(n) time
        def dfs(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        return dfs(root, -math.inf, math.inf)
        #Input: root = [2,1,3]