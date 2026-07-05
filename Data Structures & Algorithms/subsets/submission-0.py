class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(i, curr):
            nonlocal ans
            if i > len(nums):
                return

            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                back(j + 1, curr)
                curr.pop()

        back(0, [])
        return ans


        