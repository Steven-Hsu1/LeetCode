class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = defaultdict(list)
        for word in strs:
            new_word = "".join(sorted(word))
            sorted_word[new_word].append(word)
        res = []
        for key, lists in sorted_word.items():
            res.append(lists)
        return res