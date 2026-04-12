class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, N + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[N]