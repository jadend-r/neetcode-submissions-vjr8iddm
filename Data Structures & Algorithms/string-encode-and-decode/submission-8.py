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
            leng = ""
            while s[ptr] != "#":
                leng += s[ptr]
                ptr += 1
            ptr += 1
            leng = int(leng)
            decoded.append(s[ptr:ptr+leng])
            ptr += leng

        return decoded