class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Similar idea as combination sum 1
        Base case: if sum of arr > target, return, 
        sum of arr == target, copy and put into res
        Constraint: can choose a candidate at most once
        Choices: either use the candidate and move on or 
        don't use the candidate and move on. This way, we only use each 
        candidate at most once.
        Result: return the res arr
        """
        res = []
        candidates.sort()
        def backtrack(arr, index, total):
            if total == target:
                res.append(arr[:])
                return
            if index >= len(candidates) or total > target:
                return

            # use and move on
            arr.append(candidates[index])
            backtrack(arr, index + 1, total + candidates[index])
            arr.pop()
            # don't use and skip all elements that aren't unique
            i = index + 1
            while i < len(candidates) and candidates[index] == candidates[i]:
                i += 1
            backtrack(arr, i, total)
        backtrack([], 0, 0)
        return res

