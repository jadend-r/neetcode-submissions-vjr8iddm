class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += str(length) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length 

        return res
