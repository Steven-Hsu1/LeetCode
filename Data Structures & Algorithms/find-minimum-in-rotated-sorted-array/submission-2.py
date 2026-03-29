class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1
                if l >= len(nums) - 1:
                    break
                print(f"l is : {l}")
            else:
                r = mid - 1
                if r <= 0:
                    break
                print(f"r is : {r}")
        return nums[l]