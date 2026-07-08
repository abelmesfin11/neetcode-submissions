class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Algorithm:

        do dfs from every edge and mark them as -1

        then search grid and if "O", change to X, 

        if -1 change back to "O"

        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O":
                return 

            board[r][c] = -1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == -1:
                    board[i][j] = "O"
 



