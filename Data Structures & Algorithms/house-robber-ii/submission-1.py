class Solution:
    def rob(self, nums: List[int]) -> int:
        def house1(nums):
            memo = {}
            def dfs(i):
                if i >= len(nums):
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
                return memo[i]

            return dfs(0)

        return max(house1(nums[1:]), house1(nums[:-1])) if len(nums) > 1 else nums[0]

        

        