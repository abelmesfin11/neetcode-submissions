class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            if target - nums[i] in mapp:
                return [mapp[target - nums[i]], i]
            mapp[nums[i]] = i
        