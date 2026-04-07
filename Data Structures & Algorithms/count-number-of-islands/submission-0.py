class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return 0 
            if grid[row][col] == "0" or (row, col) in visited:
                return 0
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                else:
                    islands += dfs(r, c)
        return islands
