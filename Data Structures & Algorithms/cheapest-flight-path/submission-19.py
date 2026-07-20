class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #shortest path on DAG
            #cant use dijskatra's because we are constrained to k stops
        #brute forcec try every dfs path from source -> dst
            #if stops <= k, update the min price, O(N^k) time
        #O(n) utilize bellman ford relax edges k - 1

        price = [math.inf] * n
        price[src] = 0

        #relax edges k - 1 times
        #O(N * k * E)
        for i in range(k + 1):
            temp = price.copy()
            for sc, dt, cost in flights:
                if price[sc] != math.inf:
                    temp[dt] = min(temp[dt], cost + price[sc])
            price = temp
        return price[dst] if price[dst] != math.inf else -1

        #flights=[[0,1,100],[1,2,100],[0,2,500]]
        #[0, inf, inf]
            ##[0, 100, 500]
        #[0, 100, 500]
            ##[0, 100, 200]