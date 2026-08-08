class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        memo = {}
        def dp(i, color):
            if (i, color) in memo:
                return memo[(i, color)]
            
            if i == len(costs):
                return 0

            if color == 0:
                memo[(i, color)] = min(costs[i][0] + dp(i+1, 1), costs[i][0] +dp(i+1, 2))

            elif color == 1:
                memo[(i, color)] = min(costs[i][1] +dp(i+1, 0), costs[i][1] +dp(i+1, 2))

            else:
                memo[(i, color)] = min(costs[i][2] +dp(i+1, 0), costs[i][2] +dp(i+1, 1))

            return memo[(i, color)] 
        
        return min(dp(0,0), dp(0, 1), dp(0, 2))

        