class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * n
        for i in range(1, n):
            prefixProd[i] = nums[i-1] * prefixProd[i-1]
        right = 1
        for i in range(n - 1, -1, -1):
            prefixProd[i] = prefixProd[i] * right
            right = right * nums[i]
        return prefixProd

