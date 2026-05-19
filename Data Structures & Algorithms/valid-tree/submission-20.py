class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for adjacent in adj[node]:
                dfs(adjacent)
        dfs(0)
        return len(visited) == n

            