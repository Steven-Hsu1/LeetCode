class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for h in range(2, n + 1):
            dp[h] = max(dp[h - 1], dp[h - 2] + nums[h - 1])
        return dp[n]