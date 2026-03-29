class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temperature = temperatures[i]
            while stack and stack[-1][0] < temperature:
                index = stack[-1][1]
                result[index] = i - index
                stack.pop()
            stack.append((temperature, i))
        return result


