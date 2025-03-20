class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        '''
        approach: First thought, isn't this just dijkstra's but modified to bitwise AND the weights? 
        Although I don't know how to code that up. Review.
        Ok after watching NeetCode video, can't use dijkstra since cost could potentially get smaller so basically
        the case with negative weights where dijkstra doesn't backtrack to see if there are any smaller weights.
        Then he did the solution with union find. Not familiar. Going to attempt the bfs solution.
        First step is getting the components. Second is getting the cost of the components since you should always take
        the longest path to reach the destination since x & y will only ever get smaller unless y = x.
        Third step is to iterate through the queries and get the cost.
        '''
        # first create an adjacency map
        adj_map = defaultdict(set)
        for i, j, w in edges:
            adj_map[i].add((j, w))
            adj_map[j].add((i, w))
        
        def bfs(adj_map, node, visited, components, component_count):
            # two's complement makes -1 equal to all ones so -1 AND x = x.
            component_cost = -1
            queue = deque()
            queue.append(node)
            visited[node] = True
            while queue:
                node = queue.popleft()
                components[node] = component_count
                for neighbor, weight in adj_map[node]:
                    component_cost &= weight
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return component_cost

        # getting components and cost
        visited = [False] * n
        components = [0] * n
        component_count = 0
        component_cost = []
        for node in range(n):
            if not visited[node]:
                cost = bfs(adj_map, node, visited, components, component_count)
                component_count += 1
                component_cost.append(cost)
        print(component_cost)
        # run through each query. If they are in the same component, get the cost of component. else -1
        res = []
        for start, end in query:
            if components[start] == components[end]:
                res.append(component_cost[components[start]])
            else:
                res.append(-1)
        return res
        