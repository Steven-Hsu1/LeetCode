class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = defaultdict(list)
        # 0 -> 1
        # visited: 
        # 
        for a, b in prerequisites:
            adj[a].append(b)
        visited = set()
        pre = set()
        def dfs(node):
            if node in visited:
                return False
            if node in pre:
                return True
            visited.add(node)
            for other_node in adj[node]:
                if not dfs(other_node):
                    return False
            visited.remove(node)
            pre.add(node)
            res.append(node)
            return True

        
        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return res