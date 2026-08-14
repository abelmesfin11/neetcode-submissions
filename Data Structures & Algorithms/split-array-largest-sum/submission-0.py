class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            currSum = 0
            for num in nums:
                currSum += num
                if currSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                r = m - 1
                res = m
            else:
                l = m + 1
        return res