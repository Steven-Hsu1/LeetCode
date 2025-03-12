class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        '''
        log n solution is probably binary search. Find the minimum positive integer index and
        then use the len of array to calculate number of pos and neg and find the maximum between them
        Obviously O(n) time is pretty easy to see
        '''
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        r -= 1
        while r >= 0 and nums[r] == 0: #mistake here where i didn't check to make sure right was in bounds
            r -= 1
        return max(len(nums) - l, r + 1)