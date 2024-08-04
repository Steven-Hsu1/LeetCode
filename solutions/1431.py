class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxCandies = max(candies)
        for i in candies:
            if i + extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        return res