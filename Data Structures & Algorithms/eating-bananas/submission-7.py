class Solution:
    # O(n log m)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r: # O(log m)
            mid = (l + r) // 2
            totalTime = 0
            for pile in piles: # O(n)
                totalTime += math.ceil(pile / mid)
            if totalTime <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
