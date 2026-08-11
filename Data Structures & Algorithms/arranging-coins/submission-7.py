class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        largest k such that k * (k + 1) / 2 <= n
        """
        l, r = 1, n + 1
        res = 0

        while l < r:
            m = (l + r) // 2
            c = (m * (m + 1)) // 2
            if c > n:
                r = m
            else:
                l = m + 1
                res = max(res, m)

        return res
        



        
   