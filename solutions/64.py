class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #2D dp approach (easier to understand)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        # need to initialize the first row and column since other values dependant on those
        # cols
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # rows
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m-1][n-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #1D dp (going by the rows)
        #intuition: we only need information from the previous row (i-1) and the previous element
        #in the same row (j-1). We only need a size n array to store the dp information 
        #since n elements in each row
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        dp[0] = grid[0][0]

        # initialize dp for first row
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
