class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowStorage = set()
            for j in range(9):
                if board[i][j] in rowStorage:
                    return False
                if board[i][j] != ".":
                    rowStorage.add(board[i][j])
        i = 0
        j = 0
        for i in range(9):
            colStorage = set()
            for j in range(9):
                if board[j][i] in colStorage:
                    return False
                if board[j][i] != ".":
                    colStorage.add(board[j][i])
        
        squares = {}
        for i in range(9):
            for j in range(9):
                if (i // 3, j // 3) in squares and board[i][j] in squares[(i // 3, j // 3)]:
                    return False
                if board[i][j] != ".":
                    if (i // 3, j // 3) not in squares:
                        squares[(i // 3, j // 3)] = set()
                    squares[(i // 3, j // 3)].add(board[i][j])
        return True


