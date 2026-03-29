class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N
        stack = []
        for index, temp in enumerate(temperatures):
            start = index
            while stack and temperatures[stack[-1]] < temp:
                start = stack.pop()
                res[start] = index - start
            stack.append(index)
        return res