class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([c for c in s if c.isalnum()]).lower()
        return clean == clean[::-1]