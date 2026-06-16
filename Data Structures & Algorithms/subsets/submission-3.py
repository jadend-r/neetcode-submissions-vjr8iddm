class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        #O(n*2^n) time
        #O(n) auxillary space
        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy()) #O(n)
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

        #nums = [1,2,3]
        #res = [[1, 2, 3], [1, 2]]
        #[1]
            #[1, 2]
                # [1, 2, 3]
                # [1, 2]
            #[1, 3]
