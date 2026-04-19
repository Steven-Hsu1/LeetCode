class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # n log k since creating nums = O(N) and each pop is log time and we do that k times
        nums = [-num for num in nums]
        heapq.heapify(nums)
        print(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -nums[0]
        

