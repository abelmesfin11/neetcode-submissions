class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        
        for src, dest, w in times:
            adj[src].append((dest, w))

        shortest = {}
        minHeap = [(0, k)] # weight, node
        t = 0

        while minHeap:
            wei, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = wei
            t = wei
            for dest, w in adj[node]:
                if dest not in shortest:
                    heapq.heappush(minHeap, (w + wei, dest))

        return t if len(shortest) == n else -1







            


        
    
        