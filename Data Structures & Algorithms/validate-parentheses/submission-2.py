class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose = { "(" : ")" , "{" : "}", "[" : "]"}
        for char in s:
            if char in openClose:
                stack.append(char)
            else:
                if stack and openClose[stack[-1]] != char or not stack:
                    return False
                stack.pop()
        return len(stack) == 0
        