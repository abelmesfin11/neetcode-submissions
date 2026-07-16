class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)


        def dfs(src, path):
            if src in path:
                return False

            if src in visit:
                return True
            
            visit.add(src)
            path.append(src)

            for nei in graph[src]:
                if not dfs(nei, path):
                    return False

            topSort.append(src)
            path.pop()
            return True

        topSort = []
        visit = set()
        for i in range(numCourses):
            if not dfs(i, []):
                return False
        return True

