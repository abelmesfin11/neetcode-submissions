class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []
        for num in count.keys():
            heapq.heappush(maxHeap, (-count[num], num))
    
        ans = []
        while k > 0:
            ans.append(heapq.heappop(maxHeap)[1])
            k -= 1
        return ans
        