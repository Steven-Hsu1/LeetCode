class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        '''
        Idea: To get the number of possible subarrays without
        the alternating restriction, it's just the index i + 1.
        ie if we are at index 2, we can create 3 subarrays. Now
        since we have a restriction of alternating subarrays,
        we keep track of the last time we have seen an alternating
        sequence so we subtract that from index i since any subarray
        we create after will have the alternating sequence, hence
        we don't include it
        '''
        lastAlt = -1
        res = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                lastAlt = i - 1
            res += (i - lastAlt)
        return res