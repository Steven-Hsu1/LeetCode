class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return math.sqrt((x ** 2) + (y ** 2))
        closest = []
        res = []
        for x, y in points:
            heapq.heappush(closest, (euclidean_distance(x, y), [x, y]))
        
        while k > 0:
            arr = heapq.heappop(closest)[1]
            res.append(arr)
            k -= 1
        return res