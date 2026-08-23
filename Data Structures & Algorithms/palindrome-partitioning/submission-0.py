class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def back(i, curr):
            if i >= len(s):
                ans.append(curr[:])
                return 

            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.isPali(sub):
                   curr.append(sub)
                   back(j+1, curr)
                   curr.pop()

        back(0, [])
        return ans

    def isPali(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
        

  
