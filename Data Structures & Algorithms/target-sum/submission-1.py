from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])
            return add + sub

        return dfs(0, 0)
