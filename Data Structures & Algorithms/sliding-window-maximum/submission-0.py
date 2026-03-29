class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # idea is that for each window of length k, we maintain a heap
        # so getting the max element is O(1). But we don't care about
        # elements that aren't the max so we just keep track of if the
        # top element is in our current window, if not, we can just
        # pop it since we won't use it again. 
        res = []
        heap = []
        heapq.heapify(heap)
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            if r + 1 >= k: # check if we have a big enough window yet
                while heap[0][1] <= r - k:
                    heapq.heappop()
                res.append(-heap[0][0])
        return res