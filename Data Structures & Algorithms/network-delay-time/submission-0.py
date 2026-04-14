class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, time)
            for nei, time2 in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + time2, nei))
        return t if len(visited) == n else -1