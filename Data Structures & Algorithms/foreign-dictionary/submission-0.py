class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # first we need to form a graph
        # def build_adj(word1, word2):
        #     for c1, c2 in zip_longest(word1, word2, fillvalue = ""):
        #         if c1 != c2:
        #             return (c1, c2)
        #     return ""
                
        # adj = defaultdict(set)
        # indegree = defaultdict(int)
        # for i in range(len(words)):
        #     for j in range(i + 1, len(words)):
        #         word1, word2 = words[i], words[j]
        #         a, b = build_adj(word1, word2)
        #         if a in adj and b in adj[a]:
        #             continue
        #         adj[a].add(b)
        #         indegree[b] += 1
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        print(adj)
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        if len(res) != len(indegree):
            return ""

        return "".join(res)

        # should form a DAG if there is a proper ordering
        # if there is a cycle, can't be correct return ""
        # run toposort


