class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums)
        while l <= r:
            mid = l + (r - l) // 2
            index = 0
            count = 0
            while index < len(nums):
                if nums[index] <= mid:
                    index += 2
                    count += 1
                else:
                    index += 1
            if count < k:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res