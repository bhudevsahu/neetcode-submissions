class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in closeToOpen:
                if not stack or closeToOpen[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return not stack