class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        l, r = 1, max(ribbons)
        res = 0
        while l <= r:
            m = (l + r) // 2
            if self.is_possible(m, ribbons, k):
                l = m + 1
                res = max(res, m)
            else:
                r = m - 1
        return res

    def is_possible(self, x, ribbons, k):
        total_ribbons = 0
        for ribbon in ribbons:
            total_ribbons += ribbon // x
            if total_ribbons >= k:
                return True
        return False

    


    
        