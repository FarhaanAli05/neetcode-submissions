class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        closed_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in closed_to_open and not stack:
                return False
            if i in closed_to_open and stack[-1] == closed_to_open[i]:
                stack.pop()
                continue
            stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True