class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

   
        def dfs(src, path):
            if src in path:
                return False
            
            if src in visited:
                return True

            visited.add(src)
            path.append(src)
            
            for nei in graph[src]:
                if not dfs(nei, path):
                    return False

            topSort.append(src)
            path.pop()
            return True
        
        topSort = []
        visited = set()
        for i in range(numCourses):
            if not dfs(i, []):
                return []
        return topSort
            