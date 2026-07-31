class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True
        while changed:
            changed = False
            l = arr[0]
            for i in range(1, len(arr) - 1):
                curr = arr[i]
                if arr[i] < l and arr[i] < arr[i + 1]:
                    arr[i] += 1
                    changed = True
                if arr[i] > l and arr[i] > arr[i + 1]:
                    arr[i] -= 1
                    changed = True
                l = curr
        return arr

        