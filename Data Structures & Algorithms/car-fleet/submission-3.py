class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psList = list(zip(position, speed))
        psList.sort(key=lambda x: x[0], reverse=True)
        stack = [psList[0]]
        for ps in psList[1:]:
            timeLeft = (target - ps[0]) / ps[1]
            if (target - stack[-1][0]) / stack[-1][1] < timeLeft: # Car fleet ahead of us will reach there in less time, so we're a new fleet
                stack.append(ps)
        return len(stack)