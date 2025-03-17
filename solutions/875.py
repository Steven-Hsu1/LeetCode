class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We use binary search where the search space must be from 1 to max(piles)
        # since h is at least len(piles), we will never need to take a higher rate
        # than the max element of piles as the rate and the min rate has to be 1 banana per hour
        # Now we have to find the condition. If we use more hours than we have, we must increase the rate
        # so we can finish the bananas faster. If we don't use up all the hours, we must decrease the rate
        l, r = 1, max(piles)
        res = r
        while l < r:
            hours = h
            mid = l + (r - l) // 2
            for pile in piles:
                hours -= math.ceil(pile / mid)
            if hours < 0:
                l = mid + 1
            else:
                r = mid
                res = mid
        return res            
