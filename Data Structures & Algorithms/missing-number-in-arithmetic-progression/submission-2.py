class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference = (arr[n - 1] - arr[0]) // n

        lo = 0
        hi = n - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid] == arr[0] + mid * difference:
                lo = mid + 1
            else:
                hi = mid
        return arr[0] + difference * hi