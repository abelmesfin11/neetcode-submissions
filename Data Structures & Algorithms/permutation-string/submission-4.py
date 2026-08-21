class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:k])

        if c1 == c2:
            return True

        for r in range(k, len(s2)):
            c2[s2[r]] += 1
            c2[s2[r-k]] -= 1

            if c2[s2[r-k]] == 0:
                del c2[s2[r-k]]

            if c1 == c2:
                return True

        return False

    
             
            

        
        