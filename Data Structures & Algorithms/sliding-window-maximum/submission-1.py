class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #o(n^2) two pointers l r, each iteration iterate through window and find the max
        res = []
        l = 0
        for r in range(k-1, len(nums)):
            maxElem = -math.inf
            for i in range(l, r+1):
                if nums[i] > maxElem:
                    maxElem = nums[i]
            res.append(maxElem)
            l += 1
        return res
            