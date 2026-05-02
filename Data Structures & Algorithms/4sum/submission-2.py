class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums.sort()
        # [-5, -2, 3, 4, 6] target = 11
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, N):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, N - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return res


