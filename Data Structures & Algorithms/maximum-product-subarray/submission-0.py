class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            temp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * temp, n * curMin, n)
            res = max(curMax, res)
        return res


