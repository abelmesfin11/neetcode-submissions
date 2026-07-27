class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                continue
            else:
                count += 1
                if s[i - 1] == " ":
                    break
        return count
            
       