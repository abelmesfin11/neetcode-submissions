class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [nums[0]]
        tot = sum(nums)

        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])

        if tot - nums[0] == 0:
            return 0

        
        for i in range(1, len(nums)):
            if pref[i-1] == tot - pref[i]:
                return i
        return -1
        