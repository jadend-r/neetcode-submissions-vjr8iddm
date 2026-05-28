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

        def backtrack(src):
            # two base cases
            # 1. if len(res) == n + 1, all edges traversed 
                # n tickets visits n + 1 cities 
            if len(res) == len(tickets) + 1:
                return True
            # 2. node not in adj (no outgoing edges, dead end)
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, nei in enumerate(temp):
                # backtrack
                res.append(nei) # add city to itinerary
                adj[src].pop(i) # remove from graph
                if backtrack(nei): return True
                res.pop()          #undo choice, hit a dead end down this path
                adj[src].insert(i, nei)
            return False
        backtrack("JFK")
        return res