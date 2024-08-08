class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        direction = 1
        row, col = 0, 0
        while rows > 0 and cols > 0:
            for _ in range(cols):
                res.append(matrix[row][col])
                col += direction
            col -= direction  # Step back after loop since final iteration makes col OOB
            row += direction  # Move down for the next loop
            # since we have traversed all items in a singular row, remove that row
            rows -= 1
            for _ in range(rows):
                res.append(matrix[row][col])
                row += direction
            row -= direction  # Step back after loop since final iteration makes row OOB
            col -= direction  # Move left for the next loop
            # since we have traversed all items in a singular col, remove that col
            cols -= 1
            direction *= -1
        return res