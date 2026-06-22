class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res




# stk = [36]
# res = [1, ]
# [30,38,30,36,35,40,28]
# [1,2, 1]