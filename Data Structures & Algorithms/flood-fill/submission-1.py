class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        original = image[sr][sc]

        image[sr][sc] = color
        dxs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        m = len(image)
        n = len(image[0])
        q = deque([(sr, sc)])
     
        while q:
            r, c = q.popleft()
            for dx, dy in dxs:
                nr = r + dx
                nc = c + dy
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                    image[nr][nc] = color
                    q.append((nr, nc))
        return image

        




         