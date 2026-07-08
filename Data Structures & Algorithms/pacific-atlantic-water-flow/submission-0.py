class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visited or prevHeight > heights[r][c]:
                return 

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for i in range(n):
            dfs(0, i, pac, -float('inf'))

        for i in range(m):
            dfs(i, 0, pac, -float('inf'))

        for j in range(m):
            dfs(j, n-1, atl, -float('inf'))

        for j in range(n):
            dfs(m-1, j, atl, -float('inf'))


        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res

        