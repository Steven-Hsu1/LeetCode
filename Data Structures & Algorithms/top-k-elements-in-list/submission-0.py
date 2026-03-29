'''
Obvious idea is to create a Counter map and then sort that based on the freq and grab
the top k elements but that is O(nlogn). 
[5,5,1,2,3,3,3]
I remember something about this. We create a custom hash function where each bucket points to 
another bucket so imagine I have a map 5: 2, 1: 1, 2: 1, 3: 3 and I store an array of unique
elements [5,1,2,3] so 

Ok just watched neetcode explaination without code. It does have something to do with buckets, but
wrong idea. What we should notice is that we can have a map from 
counts -> [values]. Since counts is bounded by n, we just have to iterate through backwards
to find which values represent these counts.
'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        mp = {i: [] for i in range(len(nums) + 1)}
        for num, count in counts.items():
            mp[count].append(num)
        print(mp)
        res = []
        for i in range(len(nums), -1, -1):
            for element in mp[i]:
                res.append(element)
                if len(res) == k:
                    return res
        return res