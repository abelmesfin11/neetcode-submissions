class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)
        for num in arr:
            if num + diff not in arr:
                return num + diff
        
        return arr[0]

        

   
