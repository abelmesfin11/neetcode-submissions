class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1 = []
        w2 = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                w1.append(i)
            elif wordsDict[i] == word2:
                w2.append(i)

        dist = float('inf')
        for i in w1:
            for j in w2:
                dist = min(dist, abs(i-j))
        return dist
        