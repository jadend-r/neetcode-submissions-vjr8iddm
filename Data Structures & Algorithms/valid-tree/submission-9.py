class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # CAN ALSO DO UNION FIND
        if len(edges) != n - 1:
            return False
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) #path compression
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return False

        return True
        # if not n:
        #     return True
            
        # adj = collections.defaultdict(list)
        # visited = set()
        # for n1, n2 in edges:
        #     adj[n1].append(n2)
        #     adj[n2].append(n1)

        # def dfs(node, parent=None):
        #     if node in visited:
        #         return False

        #     visited.add(node)
        #     for adjacent in adj[node]:
        #         if adjacent == parent:
        #             continue
        #         if not dfs(adjacent, node):
        #             return False

        #     return True

        # if dfs(0) and len(visited) == n:
        #     return True

        # return False