class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, arr):
            if index == len(nums):
                res.append(arr[:])
                return
            # include element
            arr.append(nums[index])
            backtrack(index + 1, arr)
            arr.pop()

            # don't include
            backtrack(index + 1, arr)
        backtrack(0, [])
        return res