class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if i < 0:
                return 0
            if remaining < 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i-1, remaining)
            return memo[(i, remaining)]
        return dfs(len(coins) -1,amount)