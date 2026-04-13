class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        resIdx = 0
        resLen = 0
        memo = {}
        def isPalin(l, r):
            if l >= r:
                return True
            if (l, r) in memo:
                return memo[(l, r)]
            if s[l] == s[r]:
                memo[(l, r)] = isPalin(l + 1, r - 1)
            else:
                memo[(l, r)] = False
            return memo[(l, r)]

        for i in range(N):
            for j in range(i, N):
                if isPalin(i, j):
                    currentLen = j - i + 1
                    if currentLen > resLen:
                        resLen = currentLen
                        resIdx = i
        return s[resIdx : resIdx + resLen]