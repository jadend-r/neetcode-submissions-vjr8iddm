class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = 0
        self.prevMin = {}

    def push(self, val: int) -> None:
        if len(self.stack) > 0 and val < self.stack[self.minIndex]:
            self.prevMin[len(self.stack)] = self.minIndex
            self.minIndex = len(self.stack)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) - 1 == self.minIndex and len(self.stack) > 1:
            self.minIndex = self.prevMin[len(self.stack) - 1]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minIndex]

