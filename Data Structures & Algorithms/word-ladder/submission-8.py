class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        wordSet.add(endWord)
        g = defaultdict(list)

        for word in wordSet:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                g[pat].append(word)
        
        q = deque([(beginWord, 1)])
        seen = {beginWord}

        while q:
            word, cnt = q.popleft()
            if word == endWord:
                return cnt
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                for w in g[pat]:
                    if w not in seen:
                        seen.add(w)
                        q.append((w, cnt + 1))

        return 0



                   

            



        