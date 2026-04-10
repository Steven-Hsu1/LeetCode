class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        connected_components = 0
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
            
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                connected_components += 1
        return connected_components
                