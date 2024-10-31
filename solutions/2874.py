class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        max_left = [0] * n
        max_left[0] = nums[0]
        # keep a running maximum from the left so i-1 would be the index for the first element.
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i])
        max_right = nums[-1]
        for i in range(n - 2, 0, -1):
            ans = max(ans, (max_left[i-1] - nums[i]) * max_right)
            max_right = max(nums[i], max_right)
        return ans