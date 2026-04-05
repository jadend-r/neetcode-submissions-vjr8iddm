class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort()
        stack = []

        for p, s in ps[::-1]:
            timeLeft = (target - p) / s
            stack.append(timeLeft)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)