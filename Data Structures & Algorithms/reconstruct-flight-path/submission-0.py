class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. sort tickets alphabetically
        tickets.sort()
        # 2. build adj list (directed graph) edge source -> dest
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
        # 3. Backtrack starting from JFK 
        res = ["JFK"]

        def backtrack(node):
            # two base cases
            # 1. if len(res) == n - 1, all edges traversed 
            if len(res) == len(tickets) + 1:
                return True
            # 2. node not in adj (no outgoing edges, dead end)
            if node not in adj:
                return False

            temp = list(adj[node])
            for i, nei in enumerate(temp):
                # backtrack
                res.append(nei)
                adj[node].pop(i)
                if backtrack(nei): return True
                res.pop()
                adj[node].insert(i, nei)
        backtrack("JFK")
        return res