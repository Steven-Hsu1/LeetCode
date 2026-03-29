class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # min cost to reach step 0
        dp[1] = 0 # since we can start at either step 0 or 1
        for s in range(n):
            for i in range(1, 3): 
                if s + i <= n:
                    dp[s+i] = min(dp[s + i], dp[s] + cost[s])
        return dp[n]