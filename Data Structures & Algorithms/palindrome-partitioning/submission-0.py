class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        
        def backtrack(arr, index):
            if index >= len(s):
                res.append(arr[:])
                return
            for j in range(index, len(s)):
                if isPalindrome(s, index, j):
                    # pick current palidrome part
                    arr.append(s[index:j+1])
                    # move to the next index that isn't part of palidrome
                    backtrack(arr, j + 1)
                    # pop to remove previous decision
                    arr.pop()
        backtrack([], 0)
        return res