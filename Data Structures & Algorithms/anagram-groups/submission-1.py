class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(str1: str, str2: str) -> bool:
            if len(str1) != len(str2):
                return False
            count = [0] * 26
            for i in range(len(str1)):
                count[ord(str1[i]) - ord('a')] += 1
                count[ord(str2[i]) - ord('a')] -= 1
            return all(c == 0 for c in count)
        res = []
        for word in strs:
            assigned = False
            for group in res:
                if isAnagram(word, group[0]):
                    group.append(word)
                    assigned = True
                    break
            if not assigned:
                res.append([word])
        return res