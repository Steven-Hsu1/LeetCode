class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        correct_row = None
        while top <= bottom:
            middle = top + (bottom - top) // 2
            if matrix[middle][0] <= target and matrix[middle][COLS - 1] >= target:
                correct_row = middle
                break
            elif matrix[middle][0] >= target:
                bottom = middle - 1
            else:
                top = middle + 1
        if correct_row != None:
            l, r = 0, COLS - 1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[correct_row][mid] == target:
                    return True
                elif target > matrix[correct_row][mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False