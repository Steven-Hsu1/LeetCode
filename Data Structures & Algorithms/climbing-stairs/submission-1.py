class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1 # number of ways to get a sum of 0
        for s in range(n):
            for i in range(1, 3):
                if s + i <= n:
                    dp[s+i] += dp[s]
        return dp[n] # should return the number of ways to get sum of n