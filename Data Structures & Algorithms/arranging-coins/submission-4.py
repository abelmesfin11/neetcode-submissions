class Solution:
    def arrangeCoins(self, n: int) -> int:
        currSum = 0
        for i in range(1, n+1):
            currSum += i
            if currSum > n:
                return i - 1

        return n

        
   