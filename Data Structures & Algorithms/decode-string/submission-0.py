class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                mult = ""
                inner = ""
                while stack and stack[-1] != "[":
                    inner = stack.pop() + inner
                stack.pop() 
                
                while stack and stack[-1] in "0123456789":
                    mult = stack.pop()  + mult
                stack.append(int(mult) * inner)
            
            else:
                stack.append(ch)

        return "".join(stack)
        