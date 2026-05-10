class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                maxOpen += 1
                minOpen += 1
            elif s[i] == ')':
                minOpen -= 1
                maxOpen -= 1
            elif s[i] == "*":
                maxOpen += 1
                minOpen -= 1
            if maxOpen < 0:
                return False
            if minOpen < 0:
                minOpen = 0

        return minOpen == 0