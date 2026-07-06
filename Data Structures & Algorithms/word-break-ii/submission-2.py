class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def dfs(i, curr):
            if i == len(s):
                res.append(" ".join(curr[:]))
                return
     
            for word in set(wordDict):
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    curr.append(s[i : i + len(word)])
                    dfs(i + len(word), curr)
                    curr.pop()
        dfs(0, [])
        return res

        