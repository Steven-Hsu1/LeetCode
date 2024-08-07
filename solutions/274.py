class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        # at some point in the sorted array, the condition that the ith paper 
        # citations >= the number of papers we've seen so far is going to be 
        #false so that's the point where we stop incrememnting our hindex
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index
