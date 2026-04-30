class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        This is just unbounded knapsack
        """
        dp = defaultdict(int)
        dp[0] = 1
        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp[total - num]
        return dp[target]

