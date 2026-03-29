class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        close_open_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif close_open_map[ch] == stack[-1]:
                stack.pop()
        return len(stack) == 0