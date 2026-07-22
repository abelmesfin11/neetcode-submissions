class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        shortest = {}
        minHeap = [(grid[0][0], 0, 0)]
        drxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in shortest:
                continue

            if (r, c) == (n-1, n-1):
                return t 

            shortest[(r, c)] = t
            for dx, dy in drxs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in shortest:
                    t_new = max(t, grid[nr][nc])
                    heapq.heappush(minHeap, (t_new, nr, nc))
