class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(subarraySum):
            numSubarray = 1
            total = 0
            for num in nums:
                total += num
                if total > subarraySum:
                    numSubarray += 1
                    total = num
                    if numSubarray > k:
                        return False
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left