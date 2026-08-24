class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack = []

        for c in s:
            if c in map:
                if not stack or stack[-1] != map[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0