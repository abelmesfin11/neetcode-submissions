class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # leftmost
        def bs1(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l

        # rightmost
        def bs2(nums, target):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return l

        l = bs1(nums, target)
        r = bs2(nums, target)

        if r - l > len(nums) / 2:
            return True

        return False

            


        