class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word)

        path = 1
        visited = set([beginWord])
        q = deque([beginWord])
        print(adj)
        while q:
            qLen = len(q)
            for _ in range(qLen):
                word = q.popleft()
                if word == endWord:
                    return path
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            path += 1
        return 0
                