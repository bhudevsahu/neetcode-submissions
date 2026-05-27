# I think this is a right solution but still this system is not accepting it. Verifed outside of this editor.

class Solution:

    open_parentheses = "({["
    closed_parentheses = "]})"
    parantheses_pair ={
            ']': '[',
            '}': '{',
            ')': '('
        }
    stack = []

    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            "]": "[", "}": "{", ")": "("
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)        
        return True if not stack else False
            


    def push(self, item):
        self.stack.append(item)


    def pop(self):
        return self.stack.pop() if len(self.stack) > 0 else None

    
    def peek(self):
        return self.stack[-1]