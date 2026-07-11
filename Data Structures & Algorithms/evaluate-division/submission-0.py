class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque([(src, 1.0)])
            visited = {src}

            while q:
                for _ in range(len(q)):
                    node, val = q.popleft()
                    if node == target:
                        return val
                        
                    for neigh, weight in adj[node]:
                        if neigh not in visited:
                            q.append((neigh, val * weight))
                            visited.add(neigh)

            return -1

        return [bfs(q[0], q[1]) for q in queries]

                    


        