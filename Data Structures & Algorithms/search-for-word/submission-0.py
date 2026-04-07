class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        idea: traverse each letter in grid and keep track of the index (character)
        of the word we are looking for. Then go in all 4 directions making sure to check
        for edge cases like out of bounds by using recursion. The recursion will
        stop for words that aren't the next character that we want.
        Base case: if index == len(word) - 1 and "".join(formed) == word
        constraint: None
        choices: 4 choices (directions)
        res: output true if base case is true, otherwise, return false

        """
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def backtrack(row, col, index):
            # base case
            if index == len(word):
                return True
            # bounds check
            if (row < 0 or row >= rows or col < 0 or col >= cols 
            or word[index] != board[row][col] or visited[row][col]):
                return False
            visited[row][col] = True
            res = (backtrack(row - 1, col, index + 1) or
            backtrack(row, col - 1, index + 1) or
            backtrack(row + 1, col, index + 1) or
            backtrack(row, col + 1, index + 1))
            visited[row][col] = False
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False




            
                    