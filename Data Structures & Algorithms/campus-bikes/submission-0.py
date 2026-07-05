class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        sort by distance, worker, bike

        """
        dist = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist.append((abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]), i, j))

        dist.sort()
        ans = [None] * len(workers)
        v = [False] * len(workers)
        vBikes = [False] * len(bikes)


        for _, i, j in dist:
            if not v[i] and not vBikes[j]:
                ans[i] = j
                v[i] = vBikes[j] = True
        return ans
        







        

        