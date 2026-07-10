class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        r, c = -1, 1
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    r, c = i, j
                    break
            break

        q = deque([])
        seen = set()
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] == 0 or (r, c) in seen:
                return

            seen.add((r, c))
            q.append((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(r, c)

        drxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        steps = -1 
        while q:
            steps += 1
            for _ in range(len(q)):
                r, c = q.popleft() 

                for dx, dy in drxs:
                    nr, nc = r + dx, c + dy
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue                # skip out-of-bounds
                    if (nr, nc) in seen:
                        continue                # skip already visited (first island or earlier water)
                    if grid[nr][nc] == 1:       # found second island
                        return steps
                    if grid[nr][nc] == 0:       # water – expand bridge
                        q.append((nr, nc))
                        seen.add((nr, nc))

        return 1









    
        