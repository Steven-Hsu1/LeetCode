class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        def swap(nums, i, index):
            temp = nums[i]
            nums[i] = nums[index]
            nums[index] = temp
        while i < N:
            if nums[i] <= 0 or nums[i] > N:
                i += 1
                continue
            index = nums[i] - 1
            if nums[i] != nums[index]:
                swap(nums, i, index)
            else:
                i += 1
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1
            