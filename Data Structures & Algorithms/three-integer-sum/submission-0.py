class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        target = 0
        for i in range(len(nums) - 1):
            # num is the fixed element and it becomes 2 sum w/ target == 0
            num = nums[i]
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif i != l and i != r and l != r:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # while nums[l] == nums[l-1] and l < r:
                        # l += 1

        return res
            
                

