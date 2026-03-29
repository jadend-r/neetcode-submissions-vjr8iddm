class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if i == len(temperatures) - 1:
                continue
            
            if temperatures[i] < temperatures[i + 1]:
                result[i] = 1
                stack.append(i + 1)
                continue

            if len(stack) == 0:
                continue

            if len(stack) > 0 and temperatures[i] < temperatures[stack[-1]]:
                result[i] = stack[-1] - i
                continue
            print(temperatures[i], stack[-1], temperatures, temperatures[stack[-1]])
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                continue

            nextHigherIndex = stack[-1]
            result[i] = nextHigherIndex - i

        return result
            

            