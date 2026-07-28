class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = list(pattern)
        sList = s.split(" ")

        if len(pat) != len(sList):
            return False
        
        mapp = {}
        seen = set()
        for i in range(len(pat)):
            if pat[i] in mapp and mapp[pat[i]] != sList[i]:
                return False
            if pat[i] not in mapp and sList[i] in seen:
                return False
            mapp[pat[i]] = sList[i]
            seen.add(sList[i])
        return True
    

        