class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # first find the largest element in piles
        # once we have the largest element, we do a binary search from 1 to largest_element
        # if we use more hours than we have, then we need to increase the rate
        # if we don't use up all the hours, we decrease the rate
        # we keep track of this min rate and return it
        largest_pile = max(piles) # O(n)
        l, r = 1, largest_pile
        min_rate = float('inf')
        while l <= r:
            hours = h
            mid = l + (r - l) // 2
            for pile in piles:
                hours -= math.ceil(pile / mid)
            if hours < 0:
                l = mid + 1
            else:
                r = mid - 1
                min_rate = min(min_rate, mid)
        return min_rate
