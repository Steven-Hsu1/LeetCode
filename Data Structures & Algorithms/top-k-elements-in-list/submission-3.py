from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [0, 1 -> [1], 2 -> [2], 3 -> [3], 4, 5, 6]
        '''
        ans = []
        N = len(nums)
        count = Counter(nums)
        count_to_val = [[] for _ in range(N + 1)]
        for val, count in count.items():
            count_to_val[count].append(val)
        for i in range(len(count_to_val) - 1, -1, -1):
            for element in count_to_val[i]:
                k -= 1
                ans.append(element)
                if k <= 0:
                    return ans
        return ans

