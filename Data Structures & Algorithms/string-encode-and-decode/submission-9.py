class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s  

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        ptr = 0

        while ptr < len(s):
            j = ptr
            while s[j] != "#":
                j += 1
            length = int(s[ptr:j])
            decoded.append(s[j + 1: j + 1 +length])
            ptr = j + 1 + length

        return decoded