class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]

            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0

            memo[(i, curr)] = dp(i + 1, curr + nums[i]) + dp(i + 1, curr - nums[i])

            return memo[(i, curr)]

        return dp(0, 0)
        