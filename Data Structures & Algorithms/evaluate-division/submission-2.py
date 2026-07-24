class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            graph[x].append((y, values[i]))
            graph[y].append((x, 1 / values[i]))
        def bfs(src, end):
            q = deque([(src, 1)])
            seen = {src}
            while q:
                start, value = q.popleft()
                if start == end and len(graph[start]) != 0:
                    return value
                for nei, val in graph[start]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, value * val))
            return -1
        return [bfs(src, dest) for src, dest in queries]