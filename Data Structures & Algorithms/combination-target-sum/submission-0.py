class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Choices: include current num or don't
        Base Case: if sum of arr == target or sum > target return
        Constraint: can use a num unlimited number of times
        Result: array of numbers that sum to target
        """

        res = []
        def backtrack(arr, total, index):
            if total > target or index >= len(nums):
                return
            if total == target:
                res.append(arr[:])
                return
            
            
            # use this number and don't move to next number
            arr.append(nums[index])
            backtrack(arr, total + nums[index], index)
            arr.pop()
            # skip to next number and use it next number
            backtrack(arr, total, index + 1)

        backtrack([], 0, 0)
        return res