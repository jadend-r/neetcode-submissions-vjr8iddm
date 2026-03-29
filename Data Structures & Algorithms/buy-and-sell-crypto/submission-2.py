class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for right in range(len(prices)):
            if prices[right] < prices[l]:
                l = right
            else:
                profit = max(profit, prices[right] - prices[l])
        return profit