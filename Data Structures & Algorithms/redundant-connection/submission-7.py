class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(1, len(edges) + 1):
            adj[i] = []

        def dfs(node, par):
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visited: # there is a cycle
                    return True
                visited.add(nei)
                if dfs(nei, node):
                    return True
            return False
            
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

            visited = set()
            if dfs(x, -1): # we saw it
                return [x, y]

        return []

        
        