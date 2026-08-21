class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(i, curr):

            if i == len(nums):
                ans.append(curr[:])
                return
            
            curr.append(nums[i])
            back(i+1, curr)
            curr.pop()


            back(i+1, curr)

        back(0, [])
        return ans


           



            
        