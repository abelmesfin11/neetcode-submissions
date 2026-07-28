class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            maxRight = -1
            for j in range(i+1, len(arr)):
                if arr[j] > maxRight:
                    maxRight = arr[j]
            arr[i] = maxRight
        
        arr[-1] = -1
        return arr
    
        