import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = set(string.punctuation)
        s = ''.join([c for c in s.lower() if not c in sp])
        s = s.strip()
        s = s.replace(" ", "")
        print(s)
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True