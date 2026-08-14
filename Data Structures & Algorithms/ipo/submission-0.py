class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        pick project with highest profit within capital limit
        """
        n = len(profits)
        l = sorted(zip(capital, profits))
        i = 0
        heap = []

        for _ in range(k):

            while i < n and l[i][0] <= w:
                heapq.heappush(heap, -l[i][1])
                i += 1

            if len(heap) == 0:
                return w

            w += -heapq.heappop(heap)

        return w
        