class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(curr):
            nonlocal ans
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    back(curr)
                    curr.pop()

        back([])
        return ans

            
                         