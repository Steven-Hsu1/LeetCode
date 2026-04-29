class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        shortest = len(min(strs, key=len))
        i = 0
        while i < shortest:
            letter = strs[0][i]
            for string in strs:
                if letter != string[i]:
                    return res
            res += strs[0][i]
            i += 1
        return res