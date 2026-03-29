class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 in nums:
                continue
            curr_longest = 0
            while num in nums:
                curr_longest += 1
                res = max(res, curr_longest)
                num += 1
        return res