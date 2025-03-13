class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        edge case: what if we have 3 consecutive elements? aaa [2,3,4]. Not a consideration since problem
        states we are removing the element so when we remove an 'a'; aa [3,4], elements are still consecutive so always
        take the minimum amount meaning greedy works.
        approach: we run through linearly and check consecutive elements. If there is a consecutive element, 
        check the min(neededTime[i], neededTime[i-1]) and add that to the result.
        '''
        # index_tracker = set()
        res = 0
        l, r = 0, 1
        while r < len(colors):
            if colors[l] == colors[r]:
                minTime = min(neededTime[l], neededTime[r])
                res += minTime
                if minTime == neededTime[r]:
                    r += 1
                else:
                    l = r
                    r += 1
            else:
                l = r
                r += 1
        return res