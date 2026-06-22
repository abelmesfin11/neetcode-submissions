class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back(curr, openn, closee):
            if openn == n and closee == n:
                ans.append(curr[:])
                return
            if openn < n:
                back(curr + "(", openn + 1, closee)
            if openn > closee:
                back(curr + ")", openn, closee + 1)

        ans = []
        back("", 0, 0)
        return ans
        