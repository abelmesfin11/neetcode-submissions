class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0" or (r, c) in visited:
                return 
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    num += 1
                    dfs(i, j)
        return num

