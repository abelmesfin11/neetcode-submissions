import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = []
        for gift in gifts:
            heapq.heappush(maxHeap, -gift)

        
        while k > 0:
            g = -heapq.heappop(maxHeap)
            r = math.isqrt(g) 
            heapq.heappush(maxHeap, -r)
            k -= 1

        ans = 0
        for num in maxHeap:
            ans += -num
        return ans



        