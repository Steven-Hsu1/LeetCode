class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        def compare(word1, word2):
            if len(word1) != len(word2):
                return False
            different = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    different += 1
            return True if different == 1 else False
        for i in range(len(wordList)):
            original_word = wordList[i]
            if compare(beginWord, original_word):
                adj[beginWord].append(original_word)
                adj[original_word].append(beginWord)
            for j in range(i + 1, len(wordList)):
                new_word = wordList[j]
                if compare(original_word, new_word):
                    adj[original_word].append(new_word)
                    adj[new_word].append(original_word)
        if endWord not in adj:
            return 0
        visited = set()
        def bfs(begin, distance):
            q = deque([(begin, distance)])
            while q:
                node, distance = q.popleft()
                if node == endWord:
                    return distance
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, distance + 1))
            return 0
                    

        return bfs(beginWord, 1)

        


