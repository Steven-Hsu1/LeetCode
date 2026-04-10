class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        

        '''
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)

        def dfs(node, visited):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
               if not dfs(nei, visited):
                return False
            visited.remove(node)
            return True

        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True