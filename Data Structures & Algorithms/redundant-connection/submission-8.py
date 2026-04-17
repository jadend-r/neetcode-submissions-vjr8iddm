class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            root = node - 1
            while parents[root] != root:
                parents[root] = parents[parents[root]]
                root = parents[root]
            return root

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

