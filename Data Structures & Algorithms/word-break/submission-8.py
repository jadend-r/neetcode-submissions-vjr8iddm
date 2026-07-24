class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #brute force is compute every possible way to split s into
            #max(len(wordDict)) segments
                #check all segments in wordDict
                #O(n * len(wordDict))
        #optimize to O(n) utilizing dp
        #ptr segmenting s into two halves 
            #dp[i] = :i in wordDict and j: segmentable 

        wordDict = set(wordDict)
        n = len(s) 
        dp = [False] * (n + 1)
        dp[n] = True #dp[i] = can s[i:] be broken into dict words
                            #s[len(s)] is empty so dp[len(s)] = True
                                #can be broken into 0 words
        L = max(map(len, wordDict))
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, min(n, i + L) + 1):
                if dp[j] and s[i:j] in wordDict:
                    dp[i] = True
                    break
        return dp[0]
