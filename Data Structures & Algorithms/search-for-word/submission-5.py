class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in seen or board[r][c] != word[i]:
                return False

            seen.add((r, c))

            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)

            seen.remove((r, c))

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
                    
        