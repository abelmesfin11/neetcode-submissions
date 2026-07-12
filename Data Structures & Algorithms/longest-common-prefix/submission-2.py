class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        leng = float('inf')
        shortest = ""
        for word in strs:
            if len(word) < leng:
                leng = len(word)
                shortest = word

        ans = ""
        for i in range(len(shortest)):
            for word in strs:
                if word[i] != shortest[i]:
                    return ans
            ans += shortest[i]

        return ans



     
        