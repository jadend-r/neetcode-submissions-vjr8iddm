class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #o(k * (n-k)) two pointers l r, each iteration iterate through window and find the max
        # res = []
        # l = 0
        # for r in range(k-1, len(nums)):
        #     maxElem = -math.inf
        #     for i in range(l, r+1):
        #         if nums[i] > maxElem:
        #             maxElem = nums[i]
        #     res.append(maxElem)
        #     l += 1
        # return res

        # O(k) space
        # O(n) time
        q = deque() # deque holds at most k elems at any point O(k) auxillary
        res = []

        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        return res
            