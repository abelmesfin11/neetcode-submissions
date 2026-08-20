class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailIdx = {}
        emails = []
        emailAcc = {} 
        
        m = 0
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailAcc[m] = accId
                m += 1

        graph = defaultdict(list)
        for a in accounts:
            for i in range(2, len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i - 1]]
                graph[id1].append(id2)
                graph[id2].append(id1)

        emailGroup = defaultdict(list)
        visited = [False] * m

        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, accId)

        for i in range(m):
            if not visited[i]:
                dfs(i, emailAcc[i])


        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))

        return res


   

        