class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        visited = set()
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for adjacent in adj[node]:
                if adjacent == prev:
                    continue
                if not dfs(adjacent, node):
                    return False

            return True
        
        for n1, n2 in edges[::-1]:
            #break the connection
            adj[n1].remove(n2)
            adj[n2].remove(n1)
            visited.clear()
            if dfs(1, -1) and len(visited) == len(edges):
                return [n1, n2]
            #reconnect after dfs
            adj[n1].append(n2)
            adj[n2].append(n1)

