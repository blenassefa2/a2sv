class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Dir = [[1,0],[0,1],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
        inbound = lambda a,b: 0<=a<len(board) and 0<=b<len(board[0])
        frequency = defaultdict(int)
        
        # store count of neighbors for each cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                for x,y in Dir:
                    newI, newJ = x + i, y + j
                    if inbound(newI,newJ):
                        frequency[(i,j)] += board[newI][newJ]
        
        # change the state of the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == 1 and  not(2 == frequency[(i,j)] or 3 == frequency[(i,j)]):
                    board[i][j] = 0
                elif board[i][j] == 0 and frequency[(i,j)] == 3:
                    board[i][j] = 1
                    