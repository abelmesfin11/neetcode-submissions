class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        for keyy in count.keys():
            if count[keyy] > (n // 2):
                return keyy

        