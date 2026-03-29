class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1
        for num in nums:
            if num - 1 in nums:
                continue
            curr_longest = 1
            while num + 1 in nums:
                curr_longest += 1
                res = max(res, curr_longest)
                num += 1
        return res