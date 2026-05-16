class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - 97] += 1
            s2Count[ord(s2[i]) - 97] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        if matches == 26: return True

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[r]) - 97
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] == s1Count[idx] + 1:
                matches -= 1

            idx = ord(s2[l]) - 97
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]:
                matches += 1
            elif s2Count[idx] == s1Count[idx] - 1:
                matches -= 1
            l += 1
                
        if matches == 26:
            return True
        
        return False
                


