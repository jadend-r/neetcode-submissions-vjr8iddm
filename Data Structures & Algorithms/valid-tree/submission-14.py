class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: return True

        # depth first search cycle detection
        # build adj list 
        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False #cycle detected, not a valid tree
            
            visited.add(node)
            for adjacent in adj[node]:
                if adjacent == parent:
                    continue
                if not dfs(adjacent, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

            