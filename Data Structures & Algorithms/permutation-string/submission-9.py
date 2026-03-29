class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1Counts = [0] * 26
        windowCounts = [0] * 26

        # count chars in s1
        for c in s1:
            s1Counts[ord(c) - 97] += 1

        for right in range(len(s2)):
            charIdxRight = ord(s2[right]) - 97
            charIdxLeft = ord(s2[left]) - 97
            windowCounts[charIdxRight] += 1

            if right - left + 1 < len(s1):
                continue
            if tuple(s1Counts) == tuple(windowCounts):
                return True

            windowCounts[charIdxLeft] -= 1
            left += 1
     
        return False
                


