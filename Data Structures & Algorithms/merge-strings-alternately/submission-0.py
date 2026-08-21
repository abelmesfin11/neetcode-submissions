class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        k = min(len(word1), len(word2))

        for i in range(k):
            ans.append(word1[i])
            ans.append(word2[i])

        if len(word1) > len(word2):
            ans.append(word1[i+1:])
        
        elif len(word2) > len(word1):
            ans.append(word2[i+1:])

        

        return "".join(ans)


        