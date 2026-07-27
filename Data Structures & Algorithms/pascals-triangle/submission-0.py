class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            tmp = [0] + res[-1] + [0]
            curr = []
            leng = len(tmp) - 1
            for j in range(leng):
                curr.append(tmp[j] + tmp[j+1])
            res.append(curr)
        return res
    


        



           
