class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        idea is that since we don't care about the cost, we only
        care about the max grid[i][j] along the chosen path. If we
        can find a path that leads to grid[n-1][m-1] that contains
        a smaller max grid[i][j] then that is the optimal path
        I think the idea is that we use bfs and then we keep
        track of the max grid[i][j] for each path and return the
        smallest one. Perhaps we use dijkstras instead? This way, 
        we do a modified dijkstras where instead of edge weights,
        we are keeping track of the smallest grid[i][j] and continuing
        in that path
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = []
        # pq: (elevation, row, col)
        heapq.heappush(pq, (grid[0][0], 0, 0))
        visited = set()
        visited.add((0, 0))
        while pq:
            elevation, row, col = heapq.heappop(pq)
            if row == ROWS - 1 and col == COLS - 1:
                return elevation
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    heapq.heappush(pq, (max(elevation, grid[nr][nc]), nr, nc))
                    visited.add((nr, nc))
        return grid[ROWS - 1][COLS - 1]


