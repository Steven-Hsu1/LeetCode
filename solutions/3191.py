class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        approach: just checking some examples: 0110 -> 1000 -> 1111, 1010 -> 1101 -> impossible. 
        We see that we just go through from the left and if our nums[i] == 0, we change the next
        three consecutive items. We wouldn't ever want to change anything before i since then
        1010 -> 0100, but to change the first 0 into a 1, have to change it back anyways so no point.
        For example 2: 0111 -> 1001 -> 1110 -> impossible since we still have a 0 and we don't have
        any more "room" to change it. Essentially we are squeezing the 0's to the end. 
        '''
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0 and i + 2 < len(nums):
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                res += 1
            elif nums[i] == 0 and i + 2 >= len(nums):
                return -1
        return res
