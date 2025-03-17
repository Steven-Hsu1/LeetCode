class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        '''
        approach: we need to keep track of all the pairs so first thought
        is that we use a hashmap to keep track of the freqs and check if 
        it divides evenly into 2 for each element in the map. Then count
        the number of pairs after going through the entire array and check
        if the expected amount of pairs is equal to the pairs counted.
        '''
        num_pairs = len(nums) // 2
        freq = defaultdict(int)
        pairs = 0
        for num in nums:
            freq[num] += 1
        for key, val in freq.items():
            if val % 2 != 0:
                return False
            pairs += (val / 2)
        return num_pairs == pairs