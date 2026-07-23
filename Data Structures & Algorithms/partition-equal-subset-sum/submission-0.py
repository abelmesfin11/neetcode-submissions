class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total / 2
        memo = {}

        def dp(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if i == len(nums) or curr > target:
                return False
            if curr == target and total - curr == target:
                return True
            memo[(i, curr)] = dp(i+1, curr) or dp(i+1, curr+nums[i])
            return memo[(i, curr)]
        return dp(0, 0)





            

            






        