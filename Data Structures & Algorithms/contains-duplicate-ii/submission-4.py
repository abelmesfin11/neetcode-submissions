class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # [1, 2, 3, 1]
        #  l
        #     r
        l = 0
        window = set()
        for r in range(len(nums)):
            while r - l > k:
                window.remove(nums[l])
                l += 1
        
            if nums[r] in window:
                return True

            window.add(nums[r])

        return False