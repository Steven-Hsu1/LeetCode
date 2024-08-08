class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # goes right, down, left, up
        ans = []
        steps = 1 # increment after every 2 directions
        direction = 0 # increment when change direction from directions
        while len(ans) < rows * cols:
            for _ in range(2):
                dr, dc = directions[direction]
                for _ in range(steps):
                    if (0 <= rStart < rows and 0 <= cStart < cols):
                        ans.append([rStart, cStart])
                    rStart, cStart = rStart + dr, cStart + dc
                direction = (direction + 1) % 4
            steps += 1
        return ans