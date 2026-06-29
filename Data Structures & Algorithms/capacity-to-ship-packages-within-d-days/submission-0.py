class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(cap):
            days_needed = 1
            curr = 0
            for weight in weights:
                curr += weight
                if curr > cap:
                    days_needed += 1
                    curr = weight
            return days_needed <= days
 
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            if is_possible(m):
                r = m
            else:
                l = m + 1
        return l



        