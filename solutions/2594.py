class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
        approach: we can create a search range where the min has to be at least 1 min, but the 
        max can be the least efficient mechanic working on all the cars. Now we can binary search the range
        and check if our mid (time) is feasible for the amount of cars we have. If it is, then we should decrease
        the search space by finding a smaller time r = mid - 1. Else l = mid + 1
        '''
        l, r = 1, max(ranks) * cars * cars
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            total_cars = 0
            for rank in ranks:
                total_cars += math.floor(sqrt(mid / rank))
            if total_cars < cars:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res