class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        freq = [[] for i in range(len(word) + 1)]
        for s in word:
            count[s] = 1 + count.get(s, 0)
        for s, c in count.items():
            freq[c].append(s)
        minPresses = 0
        loopCounter = 1
        incrementor = 1
        for i in range(len(freq) - 1, -1, -1):
            for s in freq[i]:
                if loopCounter % 9 == 0:
                    incrementor += 1
                    loopCounter = 1
                minPresses = minPresses + (i * incrementor)
                loopCounter += 1
        return minPresses