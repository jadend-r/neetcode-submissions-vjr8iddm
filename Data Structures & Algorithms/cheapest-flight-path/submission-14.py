class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()
            for s, d, c in flights:
                if prices[s] != math.inf and prices[s] + c < temp[d]:
                    temp[d] = prices[s] + c
            prices = temp

        return prices[dst] if prices[dst] != math.inf else -1