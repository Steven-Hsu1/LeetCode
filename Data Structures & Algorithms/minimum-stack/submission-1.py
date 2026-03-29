class MinStack:
    #idea is that we need to keep track of the minimum value so far. We can use another stack
    #and just push the minimum between the current value we are looking at and the minimum value
    #previously to get the new minimum
    #TODO: can also do a one stack approach where you are keeping track of just one variable for the
    #min instead of at each instance of push.
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
