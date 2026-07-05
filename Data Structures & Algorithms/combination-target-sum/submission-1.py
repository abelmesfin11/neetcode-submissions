class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def back(i, curr):
            nonlocal ans
            if i >= len(nums) or sum(curr) > target:
                return 

            if sum(curr) == target:
                ans.append(curr[:])
                return


            # include
            curr.append(nums[i])
            back(i, curr)
            curr.pop()

            # exclude
            back(i + 1, curr)
        
        back(0, [])
        return ans

        