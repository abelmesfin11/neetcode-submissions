class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(num) for num in digits]
        num = int("".join(digits)) + 1
        ans = []
        for i in str(num):
            ans.append(int(i))
        return ans


        