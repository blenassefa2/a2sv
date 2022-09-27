class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
           
        for i in range(9):
            y = 0
            x = set()
            for j in range(9):
                if board[i][j] != ".":
                    y += 1
                    x.add(board[i][j])
            if y != len(x):
                return False
        for j in range(9):
            y = 0
            x = set()
            for i in range(9):
                if board[i][j] != ".":
                    y += 1
                    x.add(board[i][j])
            if y != len(x):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                y = 0
                x = set()
                for k in range(3):
                    for l in range(3):
                        if board[k+i][l+j] != ".":
                            y += 1
                            x.add(board[k+i][l+j])
                if y != len(x):
                    return False
        return True