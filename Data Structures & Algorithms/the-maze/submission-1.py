class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(r, c):

            if visited[r][c]:
                return

            visited[r][c] = True

            if [r, c] == destination:
                return

            drxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in drxs:
                nr, nc = r, c
                while 0 <= nr + dx < m and 0 <= nc + dy < n and maze[nr + dx][nc + dy] == 0:
                    nr += dx
                    nc += dy
                dfs(nr, nc)

        
        dfs(start[0], start[1])
        return visited[destination[0]][destination[1]]
        