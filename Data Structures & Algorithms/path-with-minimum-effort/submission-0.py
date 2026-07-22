class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        shortest = {}
        minHeap = [(0, 0, 0)]
        drxs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(heights)
        n = len(heights[0])

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if (r, c) in shortest:
                continue

            if (r, c) == (m-1, n-1):
                return effort

            shortest[(r, c)] = effort
            for dx, dy in drxs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in shortest:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(minHeap, (new_effort, nr, nc))

        
        
