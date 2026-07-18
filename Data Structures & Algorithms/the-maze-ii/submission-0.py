class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        drxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        startR, startC = start
        destR, destC = destination

        q = deque([(startR, startC)])
        distance = [[float('inf')] * n for _ in range(m)]
        distance[startR][startC] = 0

        while q:
            r, c = q.popleft()
            for dx, dy in drxs:
                nr, nc = r, c 
                moves = distance[nr][nc]

                while 0 <= nr + dx < m and 0 <= nc + dy < n and maze[nr + dx][nc + dy] == 0:
                    nr += dx
                    nc += dy
                    moves += 1

                if moves < distance[nr][nc]:
                    distance[nr][nc] = moves
                    q.append((nr, nc))

        return -1 if distance[destR][destC] == float('inf') else distance[destR][destC] 



        