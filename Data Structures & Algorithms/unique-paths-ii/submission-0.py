from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @cache
        def dp(r, c):
            if r >= m or c >= n:
                return 0

            if obstacleGrid[r][c]:
                return 0

            if (r, c) == (m-1, n-1):
                return 1

            total = 0

            total += dp(r+1, c) + dp(r, c+1)

            return total

        return dp(0, 0)

            







        
        