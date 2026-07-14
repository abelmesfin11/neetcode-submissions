class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        curr = s2[:n]

        countS1 = Counter(s1)
        countCurr = Counter(curr)

        if countCurr == countS1:
            return True
            
        for i in range(n, len(s2)):
            countCurr[s2[i]] += 1
            countCurr[s2[i-n]] -= 1
            if countCurr == countS1:
                return True
        
        return False





        