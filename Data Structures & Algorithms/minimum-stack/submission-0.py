class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix_stack.append(min(val, self.prefix_stack[-1] if self.prefix_stack else val))

    def pop(self) -> None:
        del self.stack[-1]
        del self.prefix_stack[-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.prefix_stack:
            return self.prefix_stack[-1]
        return None
