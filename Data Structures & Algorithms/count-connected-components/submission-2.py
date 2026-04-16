class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj = collections.defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return

            visited.add(node)
            for adjacent in adj[node]:
                if adjacent == prev:
                    continue
                dfs(adjacent, node)

        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                components += 1

        return components