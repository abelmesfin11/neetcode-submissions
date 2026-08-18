class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            hours = 0
            for b in piles:
                hours += math.ceil(b / k)
            return hours <= h
              
        l, r = 1, max(piles) 
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if canEat(m):
                r = m - 1
                idx = m
            else:
                l = m + 1
        return idx
        
        
        