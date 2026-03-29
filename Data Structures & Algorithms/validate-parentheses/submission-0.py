class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue

            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if stack[-1] == opposites[c]:
                    stack.pop()
                else:
                    stack.append(c)

        return len(stack) == 0