import collections
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build the adjacency list where every destination list is a min-heap
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)

        res = []

        # 2. Use DFS to traverse the tickets
        def dfs(airport):
            # While there are still outgoing flights from this airport
            while adj[airport]:
                # Pop the lexicographically smallest destination to "use" the ticket
                next_airport = heapq.heappop(adj[airport])
                dfs(next_airport)
            
            # 3. If we break out of the while loop, we are stuck (no outbound flights left).
            # We append the airport to our result.
            res.append(airport)

        # Start the journey at JFK
        dfs("JFK")

        # 4. Because we append to `res` when we get stuck at the END of a path,
        # our itinerary is currently backwards. Reverse it before returning!
        return res[::-1]