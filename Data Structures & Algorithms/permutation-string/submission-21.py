class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #naive approach check every substring of s2 of length s1
            #count number of characters, see if it matches character count in s1
            #O(M^2 * N)

        #counting characters in s1 & s2 in hashmap
        #slide window over s2 of length s1, adding/removing characters, if counts match return true
        #O(m*n) time, o(m) space
        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        s2Count = defaultdict(int)

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1

        if s1Count == s2Count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2Count[s2[r]] += 1
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            if s1Count == s2Count:
                return True
            
            l += 1

        return False
        #Input: s1 = "abc", s2 = "lecabee"
        #{a: 1, b: 2, c:3 } {l: 1, e: 1, c: 1}
        #l = 3, r = 3
            