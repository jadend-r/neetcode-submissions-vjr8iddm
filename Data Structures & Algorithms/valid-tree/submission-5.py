class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, parent=None):
            if node in visited:
                return False

            visited.add(node)
            for adjacent in adj[node]:
                if adjacent == parent:
                    continue
                if not dfs(adjacent, node):
                    return False

            return True

        for root in range(n):
            visited.clear()
            if dfs(root) and len(visited) == n:
                return True

        return False