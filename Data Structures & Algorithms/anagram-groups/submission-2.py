class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Key insight: we can use a hashmap where each character count is a key and the values
        are the words that match that specific character count. This avoids the problem of grouping
        them at the end as well as makes it easy to code
        '''
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())
