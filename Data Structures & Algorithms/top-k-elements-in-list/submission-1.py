from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [0, 1 -> [1], 2 -> [2], 3 -> [3], 4, 5, 6]
        '''
        ans = []
        N = len(nums)
        count = Counter(nums)
        print(count)
        count_to_val = [[] for _ in range(N + 1)]
        for count, val in enumerate(count):
            count_to_val[count].append(val)
        for i in range(len(count_to_val) - 1, -1, -1):
            if count_to_val[i] == []:
                continue
            for element in count_to_val[i]:
                k -= 1
                ans.append(element)
                if k <= 0:
                    return ans
        return ans

