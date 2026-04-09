class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(row, col):
            q = deque([(row, col, 0)])
            visited = set()
            visited.add((row, col))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                r, c, dist = q.popleft()
                if grid[r][c] == -1:
                    continue
                if grid[r][c] > 0 and grid[r][c] != 2147483647:
                    grid[r][c] = min(grid[r][c], dist)
                if grid[r][c] == 2147483647:
                    grid[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, dist + 1))


        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)
