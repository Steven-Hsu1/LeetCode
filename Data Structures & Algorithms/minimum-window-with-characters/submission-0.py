class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_map, s_map = {}, {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        have, need = 0, len(t_map)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            current_char = s[r]
            s_map[current_char] = s_map.get(current_char, 0) + 1
            if current_char in t_map and s_map[current_char] == t_map[current_char]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""

            
