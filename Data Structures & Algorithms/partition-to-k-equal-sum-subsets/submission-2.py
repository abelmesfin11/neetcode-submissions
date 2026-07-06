class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums) // k
        ans = [0] * k
        nums.sort(reverse=True)

        if sum(nums) % k != 0:
            return False

        def dfs(i):
            if i == len(nums):
                return True
    
            for j in range(k):
                if ans[j] + nums[i] <= target:
                    ans[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    ans[j] -= nums[i]
                
                if ans[j] == 0:
                    break

            return False

        return dfs(0)

            




        