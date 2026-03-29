class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        for i, price in enumerate(prices):
            if i == len(prices) - 1:
                continue
            buyPrice = prices[i]
            sellWindow = prices[i+1:]
            sellPrice = max(sellWindow)
            if sellPrice - buyPrice > bestProfit:
                bestProfit = sellPrice - buyPrice

        return bestProfit
