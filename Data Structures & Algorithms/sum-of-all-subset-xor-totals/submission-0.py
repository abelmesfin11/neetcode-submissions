class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def back(i, curr):
            nonlocal res
            xorr = 0
            for num in curr:
                xorr ^= num
            res += xorr

            for j in range(i, len(nums)):
                curr.append(nums[j])
                back(j+1, curr)
                curr.pop()

        back(0, [])
        return res
        