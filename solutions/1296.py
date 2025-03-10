class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        '''
        First thought: we could brute force this by sorting the array
        and then using sliding window to check consecutive subarray elements.
        Edit: we need to keep track of their frequencies so we know what the next
        element should be (ie if we have [1,2,3,3,4,4,5,6] and we have [1,2,3,4]
        then while left not in freq continue. This would skip 2 and move to 3 which
        is where our next consecutive array should start)
        2nd Edit: We didn't need sliding window. The problem with sliding
        window is that since we are keeping track of the freqs, we just need the
        starting number to get a consecutive array. That is why we sort. The reason
        why we get the freqs is because then we just loop through and attempt to find
        a sequence and if we don't find one, we can return False.
        '''
        if len(nums) % k != 0:
            return False
        nums.sort()
        freqs = Counter(nums)
        for num in nums:
            if freqs[num] > 0:
                for curr in range(num, num + k):
                    if freqs[curr] == 0:
                        return False
                    freqs[curr] -= 1
        return True



