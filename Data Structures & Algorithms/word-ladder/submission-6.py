class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #brute try every possible transformation starting at beginWord
            #n! * n
        #optimize w directed graph
            #map pattern -> [words that match the pattern]
                #*at, b*t, ba*
                #*ag, b*g, ba*
                #ba* -> [bat, bag]
        #bfs starting from the beginWord until we find the endWord
        #insert the beginWord into wordList
        #O(V+E) time / space

        if endWord not in wordList: return 0

        adj = collections.defaultdict(list)
        #build our graph mapping patterns -> words
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)

        #bfs from the beginWord
        q = deque([beginWord])
        visited = set([beginWord])
        min_words = 1

        while q:
            qLen = len(q)
            for _ in range(qLen):
                word = q.popleft()
                if word == endWord:
                    return min_words
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            min_words += 1
        return 0

        #beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
        #{*at: [bat], b*t, ba*, *ag, b*g, *ag, }
            

            