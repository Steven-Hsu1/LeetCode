class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, bool_arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            for i in range(len(nums)):
                if not bool_arr[i]:
                    arr.append(nums[i])
                    bool_arr[i] = True
                    backtrack(arr, bool_arr)
                    arr.pop()
                    bool_arr[i] = False
        backtrack([], [False] * len(nums))
        return res