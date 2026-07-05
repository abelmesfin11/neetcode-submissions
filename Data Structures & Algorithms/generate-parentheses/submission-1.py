class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def back(curr, openn, closee):
            nonlocal ans
            if openn == closee == n:
                ans.append(curr[:])
                return 

            if openn < n:
                back(curr + "(", openn + 1, closee)
            
            if closee < openn:
                back(curr + ")", openn, closee + 1)

        back("", 0, 0)
        return ans


            
        