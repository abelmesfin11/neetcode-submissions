class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(speed):
            if speed == 0: return False
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h
            
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
        return l