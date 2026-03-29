class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        close_open_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in close_open_map:
                if stack and close_open_map[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False