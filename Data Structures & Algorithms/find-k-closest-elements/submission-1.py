class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = [] # (dist, num)

        for num in arr:
            dist = abs(num - x)
            heapq.heappush(minHeap, (dist, num))

        ans = []
        while k > 0:
            dist, num = heapq.heappop(minHeap)
            ans.append(num)
            k -= 1
        return sorted(ans)