class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, nOpen, nClose):
            if nOpen == nClose == n:
                res.append("".join(curr))

            if nOpen < n:
                curr.append("(")
                backtrack(curr, nOpen + 1, nClose)
                curr.pop()

            if nClose < nOpen:
                curr.append(")")
                backtrack(curr, nOpen, nClose + 1)
                curr.pop()

        backtrack([], 0, 0)
        return res