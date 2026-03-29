class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # This is actually not efficient in python since string
        # concat is O(n). More optimal approach is storing the 
        # validString as a "stack" and then joining it together
        # when the string becomes valid ie when len(validString)
        # is equal to 2 * n. We pop after each dfs call since
        # it's backtracking - we are reverting the decision to add
        # an open/closed parentheses for the other dfs call.
        ans = []
        def dfs(openParen, closeParen, validString):
            if len(validString) == 2 * n:
                ans.append("".join(validString))
            if openParen < n:
                validString.append("(")
                dfs(openParen + 1, closeParen, validString)
                validString.pop()
            if closeParen < openParen:
                validString.append(")")
                dfs(openParen, closeParen + 1, validString)
                validString.pop()
        dfs(0, 0, [])
        return ans