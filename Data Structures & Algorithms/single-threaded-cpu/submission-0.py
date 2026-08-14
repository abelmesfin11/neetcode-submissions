class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, t in enumerate(tasks):
            t.append(idx)
        tasks.sort(key=lambda t: t[0])

        res, heap = [], []
        i = 0
        time = tasks[0][0]

        while heap or i < len(tasks):
            # currently ready to be processed
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not heap:
                time = tasks[i][0]
            else:
                proTime, idx = heapq.heappop(heap)
                time += proTime
                res.append(idx)

        return res

#    [2,1], [3,3], [4,1], [4,4], [5,2]

#    t=2   [2,1]

#    t=3   [3,3]

#    t=6   [4,1]

#    t=7   [4,4]

#    t=11  [5,2]



