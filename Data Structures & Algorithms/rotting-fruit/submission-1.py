class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        dxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
 
        if fresh == 0:
            return 0

        ans = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dxs:
                    nr = r + dx
                    nc = c + dy
                    
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            ans += 1
        return ans if fresh == 0 else -1
        


  











        