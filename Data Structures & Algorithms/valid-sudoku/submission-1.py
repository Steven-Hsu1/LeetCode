class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # check row digits 1-9 no dups
        for row in range(n):
            seen = set()
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        # check col digits 1-9 no dups
        for row in range(n):
            seen = set()
            for col in range(n):
                if board[col][row] == ".":
                    continue
                if board[col][row] in seen:
                    return False
                seen.add(board[col][row])
        # check 3x3 sub boxes:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square%3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


