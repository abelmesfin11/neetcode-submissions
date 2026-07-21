class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]

            if curr == 0:
                return 1

            if curr < 0 or i == len(coins):
                return 0

            memo[(i, curr)] = dp(i, curr-coins[i]) + dp(i+1, curr)

            return memo[(i, curr)]

        return dp(0, amount)
