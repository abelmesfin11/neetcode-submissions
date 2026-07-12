class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            currRow = set()
            for j in range(9):
                if board[i][j] in currRow:
                    return False
                if board[i][j] != ".":
                    currRow.add(board[i][j])

        for i in range(9):
            currCol = set()
            for j in range(9):
                if board[j][i] in currCol:
                    return False
                if board[j][i] != ".":
                    currCol.add(board[j][i])

        
        starting = [(0, 0), (0, 3), (0, 6), 
                    (3, 0), (3, 3), (3, 6), 
                    (6, 0), (6, 3), (6, 6)]

        for r, c in starting:
            seen = set()
            for i in range(3):
                for j in range(3):
                    if board[r+i][c+j] in seen:
                        return False
                    if board[r+i][c+j] != ".":
                        seen.add(board[r+i][c+j])
        
        return True



        


       
