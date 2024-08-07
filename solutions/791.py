class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)

        ans = [ch*count[ch] for ch in order]
        ans.extend(filter(lambda x : x not in order, s))

        return ''.join(ans)

