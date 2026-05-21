# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # perform a preorder traversal using _ as placeholder for null 
        res = [] #O(n) space
        def dfs(node): #O(n) time #O(n) space for callstack
            if not node:
                res.append("_")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        i = 0
        def dfs(): #O(n) time and #O(n) space 
            nonlocal i
            if data[i] == "_":
                return
            root = TreeNode(data[i])
            i += 1
            root.left = dfs()
            i += 1
            root.right = dfs()
            return root 
        return dfs()


