class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bss(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) >> 1
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        left = bss(nums, target)
        right = bss(nums, target + 1) - 1
        
        if left <= right:
            return [left, right]
        return [-1, -1]

        