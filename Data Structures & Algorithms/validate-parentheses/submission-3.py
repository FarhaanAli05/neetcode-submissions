class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in closed_to_open:
                if stack and stack[-1] == closed_to_open[i]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
        return False if len(stack) > 0 else True