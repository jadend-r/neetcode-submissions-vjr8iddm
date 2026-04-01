class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            if totalTime <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
