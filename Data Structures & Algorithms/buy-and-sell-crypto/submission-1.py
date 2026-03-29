class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = 0
        res = 0
        for r in range(1, len(prices) - 1):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res