class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = {0}
        def dfs(node, parent):
            for neigh in graph[node]:
                if neigh == parent:
                    continue

                if neigh in seen:
                    return False

                seen.add(neigh)
                if not dfs(neigh, node):
                    return False
            
            return True

        return dfs(0, -1) and len(seen) == n

        
    