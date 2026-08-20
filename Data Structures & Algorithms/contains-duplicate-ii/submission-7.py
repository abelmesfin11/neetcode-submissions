class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        for i in range(len(nums)):
            if nums[i] in mapp and abs(mapp[nums[i]] - i) <= k:
                return True
            mapp[nums[i]] = i
        return False
    