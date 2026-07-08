class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        seen = set()

        dxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))

        if fresh == 0:
            return 0


        ans = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dxs:
                    nr = r + dx
                    nc = c + dy
                    
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] == 1:
                        seen.add((nr ,nc))
                        q.append((nr, nc))
                        grid[nr][nc] = 2

            ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return ans 











        