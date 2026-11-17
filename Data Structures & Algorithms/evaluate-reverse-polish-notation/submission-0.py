class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(op2 - op1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                op1, op2 = stack.pop(), stack.pop()
                stack.append(int(float(op2) / op1))
            else:
                stack.append(int(i))
        return stack.pop()