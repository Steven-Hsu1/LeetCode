class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1
        for ch in t:
            char_map[ch] = char_map.get(ch, 0) - 1
            if char_map[ch] == 0:
                del char_map[ch]
        return len(char_map) == 0