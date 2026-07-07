class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        area = 0
        def dfs(r, c):
            nonlocal area
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
      
        maxArea = 0
        for i in range(m): 
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
        