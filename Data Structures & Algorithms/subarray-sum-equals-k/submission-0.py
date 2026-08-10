class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        preSum = {0 : 1}
        ans = 0

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in preSum:
                ans += preSum[diff]

            preSum[currSum] = 1 + preSum.get(currSum, 0)
                

        return ans



