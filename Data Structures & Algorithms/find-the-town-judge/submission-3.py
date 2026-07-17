class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in trust:
            graph[x].append(y)
        

        for i in range(1, n + 1):
            out = len(graph[i])
            inn = 0
            for j in range(1, n+1):
                if i != j and i in set(graph[j]):
                    inn += 1

            if inn == n - 1 and out == 0:
                return i

        return -1



        

        
    
       
   

    
        