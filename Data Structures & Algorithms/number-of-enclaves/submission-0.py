class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        what if i do dfs from boundary and mark all cells that can be reached
        and then do counting??
        """
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return

            grid[r][c] = -1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        
        return ans


     

           
            




