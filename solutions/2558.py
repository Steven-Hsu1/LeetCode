class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_heap = [-gift for gift in gifts]
        heapq.heapify(gifts_heap)

        for i in range(k):
            max_element = -heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -math.floor(sqrt(max_element)))
        total = 0
        while gifts_heap:
            total += heapq.heappop(gifts_heap)
        return -total