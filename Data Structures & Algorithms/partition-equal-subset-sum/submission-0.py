class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        total1, total2 = 0, 0


        '''
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        N = len(nums)
        memo = [[-1] * (target + 1) for _ in range(N + 1)]

        def dfs(index, target):
            if target == 0:
                return True
            if index >= N or target < 0:
                return False
            if memo[index][target] != -1:
                return memo[index][target]
            memo[index][target] = (dfs(index + 1, target) or dfs(index + 1, target - nums[index]))
            return memo[index][target]
        return dfs(0, target)


        
        