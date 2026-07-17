class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque([])
        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    seen.add((i, j))

        drxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, steps = q.popleft()
            for dx, dy in drxs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] != -1:
                    q.append((nr, nc, steps + 1))
                    grid[nr][nc] = steps + 1
                    seen.add((nr, nc))

        




        
        