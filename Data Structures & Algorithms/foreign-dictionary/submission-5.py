class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #topogical sort/kahns algorithm

        #adj list c->b if c comes before b 
        adj = defaultdict(set)
        indegree = {c:0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c, b in zip(w1, w2):
                if c != b:
                    if b not in adj[c]:
                        adj[c].add(b)
                        indegree[b] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""
        
        res = []
        q = deque([c for c in indegree if indegree[c] == 0])

        while q:
            c = q.popleft()
            res.append(c)
            # decrement indegree of neighbors
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""