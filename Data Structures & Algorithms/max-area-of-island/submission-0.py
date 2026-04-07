class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS):
                return 0
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            return (1 + dfs(row + 1, col) +
            dfs(row - 1, col) + 
            dfs(row, col + 1) + 
            dfs(row, col - 1))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                else:
                    maxArea = max(dfs(r, c), maxArea)
        return maxArea
