class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j)) 

        while q:
            r, c = q.popleft()
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        
