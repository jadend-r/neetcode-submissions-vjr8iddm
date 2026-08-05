class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #brute force is, for every edge try to remove it, and then
            #traverse the graph to check if connected and non cyclical
            #O(E * (V + E))
        #optimize to O(E) utilizing union find
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(node): 
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        self.res = None
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                self.res = [n1, n2]
                return

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2

        for n1, n2 in edges:
            union(n1, n2)

        return self.res