class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters_map = defaultdict(int)
        for c in s:
            characters_map[c] += 1
        for c in t:
            if characters_map.get(c) is None:
                return False
            characters_map[c] -= 1
            if characters_map[c] == 0:
                del characters_map[c]
        return len(characters_map) == 0
