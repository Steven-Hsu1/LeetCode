class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea is that for each window of length k, we maintain a heap
        # so getting the max element is O(1). But we don't care about
        # elements that aren't the max so we just keep track of if the
        # top element is in our current window, if not, we can just
        # pop it since we won't use it again. 
        heap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res