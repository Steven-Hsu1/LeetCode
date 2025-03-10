class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        ch_map = set()
        for right in range(len(s)):
            while s[right] in ch_map:
                ch_map.remove(s[left])
                left += 1
            ch_map.add(s[right])
            longest = max(longest, right - left + 1)
        return longest