class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        Intuition: We want both sides to have the same sum so we
        could use prefix sum on both the left and right sides
        and find where that intersection is.
        '''
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        lsum, rsum, l, r = 0, 0, 0, n - 1
        while l < n:
            lsum += nums[l]
            rsum += nums[r]
            leftSum[l] = lsum
            rightSum[r] = rsum
            l += 1
            r -= 1
        for i in range(n):
            if leftSum[i] == rightSum[i]:
                return i
        return -1
