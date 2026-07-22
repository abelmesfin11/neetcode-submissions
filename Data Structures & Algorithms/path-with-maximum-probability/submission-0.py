class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(len(edges)):
            src, des = edges[i]
            adj[src].append((des, -succProb[i]))
            adj[des].append((src, -succProb[i]))

    
        shortest = {}
        minHeap = [(-1, start_node)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue

            if n1 == end_node:
                return -w1 if w1 < 0 else w1

            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (-(w1 * w2), n2))

        return 0
            

        

        