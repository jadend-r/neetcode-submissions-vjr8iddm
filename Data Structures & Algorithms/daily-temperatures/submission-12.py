class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        op = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day = stack.pop()
                op[day] = i - day

            stack.append(i)
        return op