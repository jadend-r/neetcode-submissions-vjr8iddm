class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        psList = list(zip(position, speed))
        psList.sort(key=lambda x: x[0], reverse=True)
        stack = [psList[0]]
        for ps in psList[1:]:
            movesLeft = (target - ps[0]) / ps[1]
            if (target - stack[-1][0]) / stack[-1][1] < movesLeft:
                stack.append(ps)
        print(stack)
        return len(stack)