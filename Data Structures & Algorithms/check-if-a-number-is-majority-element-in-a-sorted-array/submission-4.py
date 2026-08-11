class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # leftmost
        def bs1(nums, target):
            l, r = 0, len(nums)
            idx = len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m 
                    idx = m
                else:
                    l = m + 1
            return idx

        # rightmost
        def bs2(nums, target):
            l, r = 0, len(nums)
            idx = len(nums)
            while l < r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m
                    idx = m
                else:
                    l = m + 1
            return idx

        l = bs1(nums, target)
        r = bs2(nums, target)

        if r - l > len(nums) / 2:
            return True

        return False

            


        