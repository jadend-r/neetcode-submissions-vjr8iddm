class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #valid tree cannot contain cycles
        #brute force is starting from every node, explore every possible path
            # to find back edge
            # n * n!
        
        #union find to find the backedge that creates the loop
            #if backedge found -> graph not valid tree
            #O(E * N) time / O(n) space
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        #O(e*n)
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        return True

        #Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        #parent = [1, 1, 1, 1, 4]
        #rank.  = [1, 4, 1, 1, 1]