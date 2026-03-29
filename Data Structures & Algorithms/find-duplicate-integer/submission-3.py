'''
I looked at the hints: The idea is that we have a inline hash
meaning we don't need separate memory - everything can be done
inside the array since we are guarenteed that the elements are
from the range 1 to n. ie if we have the array [2,1,2,3]. We
can have the hash function value -> index. 2 -> 1. The idea of
the absolute value is that we don't have to worry when we encounter
a negative integer since it will be converted back to the original
value. Now if we hash into the same value and the value is negative,
that's when we know that element is the duplicate.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] *= -1
            if nums[index] > 0:
                return abs(nums[i])
        return 0

