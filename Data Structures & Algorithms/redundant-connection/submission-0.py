class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        # visited = set()
        def dfs(node, parent, visited):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if parent == neighbor:
                    continue
                if dfs(neighbor, node, visited):
                    return True
            return False

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
            if dfs(e1, -1, set()):
                return [e1, e2]
        return []