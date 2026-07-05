class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(i, curr):
            nonlocal ans
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for i in range(i, n+1):
                curr.append(i)
                back(i + 1, curr)
                curr.pop()
            
        back(1, [])
        return ans
            


        