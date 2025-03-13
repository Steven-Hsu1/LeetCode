class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, l, r, counter = 0):
            while l < r:
                if s[l] != s[r]:
                    if counter == 1:
                        return False
                    else:
                        return checkPalindrome(s, l + 1, r, counter + 1) or checkPalindrome(s, l, r - 1, counter + 1)
                else:
                    l += 1
                    r -= 1
            return True
        return checkPalindrome(s, 0, len(s) - 1, 0)
            