class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            length = len(stack)
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if length == 0:
                    return False
                if stack.pop() != '(':
                    return False
            elif i == '}':
                if length == 0:
                    return False
                if stack.pop() != '{':
                    return False
            elif i == ']':
                if length == 0:
                    return False
                if stack.pop() != '[':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False