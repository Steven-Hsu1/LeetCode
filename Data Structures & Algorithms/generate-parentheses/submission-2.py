class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open, close, string):
            if len(string) == 2 * n:
                res.append("".join(string))
            if open < n:
                string.append("(")
                backtrack(open + 1, close, string)
                string.pop()
            if close < open:
                string.append(")")
                backtrack(open, close + 1, string)
                string.pop()
            
        backtrack(0, 0, [])
        return res

