class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # Helper function to expand outwards from a given center
        def countPals(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1    # Expand left
                right += 1   # Expand right
            return count
        
        for i in range(len(s)):
            # Count odd-length palindromes (center is at character i)
            res += countPals(i, i)
            
            # Count even-length palindromes (center is between i and i+1)
            res += countPals(i, i + 1)
            
        return res