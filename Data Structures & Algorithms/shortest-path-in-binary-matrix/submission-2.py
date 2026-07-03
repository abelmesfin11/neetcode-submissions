class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0)])
        n = len(grid)

        dxs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        if n == 1:
            return 1

        seen = {(0, 0)}
        curr = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in dxs:
                    newR = r + dx
                    newC = c + dy
                    if 0 <= newR < n and 0 <= newC < n and (newR, newC) not in seen and grid[newR][newC] == 0:
                        q.append((newR, newC))
                        seen.add((newR, newC))
                        if (newR, newC) == (n-1, n-1):
                            return curr + 1
            curr += 1
        return -1




       

        