class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for letter in word:
                adj[letter] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        
        def dfs(src, path):
            if src in path:
                return False

            if src in visit:
                return True
            
            visit.add(src)
            path.append(src)

            for nei in adj[src]:
                if not dfs(nei, path):
                    return False

            topSort.append(src)
            path.pop()
            return True

        topSort = []
        visit = set()
        for char in adj:
            if not dfs(char, []):
                return ""

        topSort.reverse()
        return "".join(topSort)
        


        

            

        