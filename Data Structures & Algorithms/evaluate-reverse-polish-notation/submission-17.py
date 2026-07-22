class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #O(n) using stack
            #iterate thru tokens
                #1. find number -> push to stack O(1)
                #2. find an operation pop twice to get operands
                    #perform operation push back onto stack
                #3. return stack[0]

        stack = []
        #iterate thru tokens O(n) time/space
        for token in tokens:
            if token not in ('+', '-', '*', '/'): #O(1)
                stack.append(int(token))
            else:
                #found operation, pop twice to get operands and push result
                op2 = stack.pop()
                op1 = stack.pop()
                res = 0
                if token == '+':
                    res = op1 + op2
                elif token == '-':
                    res = op1 - op2
                elif token == '*':
                    res = op1 * op2
                elif token == '/':
                    res = int(op1 / op2)
                stack.append(res)
        return stack[0]
        #Input: tokens = ["1","2","+","3","*","4","-"]
        #stack = [1, 2]
            #stack = [], op1 = 1, op2 = 2 res = 3
                #stack = [3]
        #stack = [3, 3]
            #stack = [], op1 = 3, op2 = 3 res = 9
                #stack = [9]
        #stack = [9, 4]
            #stack = [], op1 = 9, op2 = 4 res = 5
                #stack = [5]
