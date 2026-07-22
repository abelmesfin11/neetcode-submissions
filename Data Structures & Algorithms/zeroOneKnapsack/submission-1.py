class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        def dp(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]

            if i == len(profit):
                return 0

            if weight[i] <= curr:
                memo[(i, curr)] = max(dp(i + 1, curr), profit[i] + dp(i + 1, curr - weight[i]))
            else:
                memo[(i, curr)] = dp(i + 1, curr)
                
            return memo[(i, curr)]

        return dp(0, capacity)
