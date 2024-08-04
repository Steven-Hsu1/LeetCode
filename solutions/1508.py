class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraySums = []
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                subarraySums.append(sum)
        subarraySums.sort()
        res = 0
        for i in range(left - 1, right):
            res += subarraySums[i]
        return res % (pow(10, 9) + 7)