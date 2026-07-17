from functools import cache

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)

        visited = set()
         
        @cache
        def dfs(node):
            if len(graph[node]) == 0:
                return node == destination
            
            # detect a cylce
            if node in visited:
                return False

            visited.add(node)
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            return True

        return dfs(source)
        


         
