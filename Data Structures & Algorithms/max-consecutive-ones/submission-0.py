class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                curr = 0
            else:
                curr += 1
            ans = max(ans, curr)
        return ans
            
            



        