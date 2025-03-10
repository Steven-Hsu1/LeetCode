class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        '''
        first thought, use a list and iterate through the nums array
        and keep track of all indices where x appears in nums. Then go through
        queries and see if it's in bounds and get the index from our array
        '''
        answer = []
        occurances = []
        for i, num in enumerate(nums):
            if num == x:
                occurances.append(i)
        for query in queries:
            if query > len(occurances):
                answer.append(-1)
            else:
                answer.append(occurances[query - 1])
        return answer
