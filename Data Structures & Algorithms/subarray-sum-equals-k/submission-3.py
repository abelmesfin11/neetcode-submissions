class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = {0 : 1}
        curr = 0
        ans = 0
        for num in nums:
            curr += num
            diff = curr - k
            if diff in preSum:
                ans += preSum[diff]
            preSum[curr] = 1 + preSum.get(curr, 0)
        return ans 
        