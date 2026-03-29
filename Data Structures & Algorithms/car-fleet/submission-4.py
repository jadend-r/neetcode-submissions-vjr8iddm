class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psList = list(zip(position, speed))
        psList.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for p, s in psList:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # This car catches up to the fleet ahead so remove it from the stack
                stack.pop()                                # because time left is smaller than before it
        return len(stack)