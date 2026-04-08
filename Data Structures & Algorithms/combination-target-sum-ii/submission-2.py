class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, comb, summ):
            if summ == target:
                res.append(comb.copy())
                return
            if summ > target or i == len(candidates):
                return

            summ += candidates[i]
            comb.append(candidates[i])
            backtrack(i + 1, comb, summ)

            comb.pop()
            summ -= candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, comb, summ)
        backtrack(0, [], 0)
        return res
