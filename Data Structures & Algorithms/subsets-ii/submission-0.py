class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def back(i, curr):
            nonlocal ans
            if i == len(nums):
                ans.append(curr[:])
                return

            # include
            curr.append(nums[i])
            back(i + 1, curr)
            curr.pop()

            # exclude
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            back(i + 1, curr)

        back(0, [])
        return ans



            
        