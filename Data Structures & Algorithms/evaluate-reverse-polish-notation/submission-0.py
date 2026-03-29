class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def perform_operation(operation_string, num1, num2):
            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y,
            }
            if operation_string in operations:
                return operations[operation_string](num1, num2)
            else:
                raise ValueError("Invalid operation")

        stack = []
        operations = set(["+", "-", "*", "/"])
        stack.append(tokens[0])
        total = 0
        for i in range(1, len(tokens)):
            print(stack)
            if tokens[i] in operations:
                second = stack.pop()
                first = stack.pop()
                total = perform_operation(tokens[i], int(first), int(second))
                stack.append(total)
            else:
                stack.append(tokens[i])
        return stack[0]