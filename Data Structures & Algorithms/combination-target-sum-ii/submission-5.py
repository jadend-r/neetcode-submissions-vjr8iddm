class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking solution skip duplicates
        #sorting the input array so duplicates end up next to each other
        # O(n log n)
        candidates.sort()

        res = []
        curr = []
        def backtrack(i, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return
            if i == len(candidates) or remaining < 0:
                return
            
            num = candidates[i]
            curr.append(num)
            backtrack(i + 1, remaining - num)

            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, remaining)
        backtrack(0, target)
        return res

