class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(openParen, closeParen, string):
            print(len(string))
            if closeParen > openParen or len(string) > 2 * n:
                return
            dfs(openParen + 1, closeParen, string + "(")
            dfs(openParen, closeParen + 1, string + ")")
            if closeParen == openParen and closeParen == n and openParen == n:
                ans.append(string)
        dfs(0, 0, "")
        return ans