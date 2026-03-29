class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26 
        windowCount = [0] * 26
        left = 0

        # Count all chars in s1
        for c in s1:
            s1Count[ord(c) - 97] += 1

        for right in range(len(s2)):
            windowCount[ord(s2[right]) - 97] += 1
            if right - left + 1 < len(s1):
                continue
            if tuple(s1Count) == tuple(windowCount):
                return True
            windowCount[ord(s2[left]) - 97] -= 1
            left += 1
          
        return False
