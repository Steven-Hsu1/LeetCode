class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited, cycle = set(), set()
        cycle_start = -1
        def dfs(node, parent):
            nonlocal cycle_start
            if node in visited:
                cycle_start = node
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node == cycle_start:
                        cycle_start = -1
                    return True
            return False
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
            