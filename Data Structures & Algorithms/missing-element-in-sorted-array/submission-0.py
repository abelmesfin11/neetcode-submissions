class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            missing = nums[mid] - nums[0] - mid

            if missing >= k:
                r = mid
            else:
                l = mid + 1
       
        return nums[0] + k + l - 1

        