class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        N = len(s)
        known = set()
        def isPalin(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        for i in range(N):
            for j in range(i, N):
                string = s[i:j+1]
                if string in known:
                    res += 1
                elif isPalin(string):
                    known.add(string)
                    res += 1
        return res
                