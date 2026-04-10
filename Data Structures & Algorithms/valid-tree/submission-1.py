class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited = set()
    
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
