class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        countsS1 = [0] * 26
        countsS2 = [0] * 26
        matches = 0

        for i in range(len(s1)):
            countsS1[ord(s1[i]) - 97] += 1
            countsS2[ord(s2[i]) - 97] += 1

        for i in range(26):
            if countsS1[i] == countsS2[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[r]) - 97
            countsS2[idx] += 1
            if countsS2[idx] == countsS1[idx]:
                matches += 1
            elif countsS2[idx] == countsS1[idx] + 1:
                matches -= 1

            idx = ord(s2[l]) - 97
            countsS2[idx] -= 1
            if countsS2[idx] == countsS1[idx]:
                matches += 1
            elif countsS2[idx] == countsS1[idx] - 1:
                matches -= 1
            l += 1
        return matches == 26