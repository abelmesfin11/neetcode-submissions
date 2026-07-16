class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(list) # pattern : word
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                graph[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        res = 1

        while q:

            word, count = q.popleft()
            if word == endWord:
                return count

            for j in range(len(word)):
                pat = word[:j] + "*" + word[j+1:]
                for neigh in graph[pat]:
                    if neigh not in seen:
                        seen.add(neigh)
                        q.append((neigh, count + 1))
            

        return 0



                

            


        