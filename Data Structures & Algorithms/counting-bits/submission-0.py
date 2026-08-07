class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.helper(i))
        return ans
        

    

    def helper(self, n):
        res = 0
        while n:
            res += 1 if n & 1 else 0
            n >>= 1
        return res

