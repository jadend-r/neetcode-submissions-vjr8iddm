class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #brute force is compute every possible way to split s into
            #max(len(wordDict)) segments
                #check all segments in wordDict
                #O(n * len(wordDict))
        #optimize to O(n) utilizing dp
        #ptr segmenting s into two halves 
            #dp[i] = :i in wordDict and j: segmentable 
                
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(dp)):
            if dp[i]:
                for j in range(i + 1, len(dp)):
                    if s[i: j] in wordDict:
                        dp[j] = True
        return dp[len(s)]
