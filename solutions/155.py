class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)
    

    def pop(self) -> None:
        if self.data:
            popped = self.data.pop()
            if self.min_stack and popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        return -1

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()