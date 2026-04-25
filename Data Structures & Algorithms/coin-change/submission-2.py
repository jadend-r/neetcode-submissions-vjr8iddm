class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        #if n == 0:
            #return 0
        dp = [math.inf] * (n + 1)
        #dp[i] = fewest num of coins to make amount i
        #dp[0] = 0
        dp[0] = 0

        for amt in range(amount + 1):
            for coin in coins:
                if amt - coin < 0:
                    continue
                dp[amt] = min(dp[amt], dp[amt-coin] + 1)

        return dp[n] if dp[n] != math.inf else -1