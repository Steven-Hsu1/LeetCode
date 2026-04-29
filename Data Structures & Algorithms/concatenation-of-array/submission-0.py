class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)
        return [nums[i % N] for i in range(2 * N)]