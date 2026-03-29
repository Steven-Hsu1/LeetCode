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
        def checkSubBox(i, j):
            seen = set()
            for row_3 in range(i, j):
                for col_3 in range(i, j):
                    if board[row_3][col_3] == ".":
                        continue
                    if board[row_3][col_3] in seen:
                        return False
                    seen.add(board[row_3][col_3])
            return True     
        for i in range(0, 7, 3):
            for j in range(3, 10, 3):
                if j - i != 3:
                    continue
                if not checkSubBox(i, j):
                    return False
        return True


