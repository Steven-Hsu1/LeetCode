class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(row, col, visit, prevHeight):
            if ((row, col) in visit or row < 0 or col < 0 or row >= ROWS or col >= COLS or heights[row][col] < prevHeight):
                return
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for j in range(COLS):
            dfs(0, j, pacific, heights[0][j])
        for j in range(COLS):
            dfs(ROWS - 1, j, atlantic, heights[ROWS - 1][j])
        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
        for i in range(ROWS):
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res