class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        perhaps we can do a modified dijkstras where we use a pq
        to iterate on the lowest stops. Wouldn't this just be bfs then?
        Since all the prices are positive, we can probably use bfs
        but we have to keep track of the path length. but since bfs
        guarentees shortest path, if the first path we find doesn't work, 
        then no path can work. But what if the case is that k is large and
        so our goal then is to find the cheapest path. could also have a dp
        arr where we are keeping track of the number of stops and cheapest price
        (maybe ordered map?)
        don't need ordered map, need to keep a distance array and set initial node
        as 0 and then for each node, we keep track of the cheapest way to get to that point
        '''
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append([to_i, price_i])

        prices = {node: float('inf') for node in range(n)}
        prices[src] = 0
        # (current_cost, src, # of stops)
        q = deque([(0, src, 0)])
        while q:
            current_cost, from_i, num_stops = q.popleft()
            if num_stops > k:
                continue
            for to_i, price_i in adj[from_i]:
                next_cost = current_cost + price_i
                if next_cost < prices[to_i]:
                    prices[to_i] = next_cost
                    q.append((next_cost, to_i, num_stops + 1))
        return prices[dst] if prices[dst] != float('inf') else -1




        