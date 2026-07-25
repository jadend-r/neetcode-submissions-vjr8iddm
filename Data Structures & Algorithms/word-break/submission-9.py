class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #len(wordDict) = W
        #brute force check all words in dict, if beginning portion
            #of string starts with any word
                #dfs to remaining portion of string and repeat
                #W^n time o(n) space for the recursion stack
        #o(n^3) optimize using dynamic programming
            #dp[i] where dp[i] means can we break s[i:] into dictionary words
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True #s[len(s)] is out of bounds, can be broken into
                            #0 dictionary words
        #iterate in reverse through s
            #each time asking is there an earlier position j
                #where s[j..n] can be broken into dict words
                    #and s[i..j] is in wordDict
        wordDict = set(wordDict)
        L = max(map(len, wordDict)) #O(W)

        #O(n^2 * L) time / o(n) space
        for i in range(len(s) - 1, -1, -1): #O(n)
            for j in range(i + 1, min(i + L + 1, len(s) + 1)): #O(L)
                if dp[j] and s[i:j] in wordDict: #O(n)
                    dp[i] = True
        return dp[0]

        #Input: s = "neetcode", wordDict = ["neet","code"]
        #dp = [True, False, False, False, True, False, False, False, True]