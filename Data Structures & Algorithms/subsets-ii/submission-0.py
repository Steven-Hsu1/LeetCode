class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(arr, index):
            if index == len(nums):
                res.append(arr[:])
                return
                
            arr.append(nums[index])
            backtrack(arr, index + 1)
            arr.pop()
            i = index
            while i < len(nums) and nums[i] == nums[index]:
                i += 1
            backtrack(arr, i)
        backtrack([], 0)
        return res
            