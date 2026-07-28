class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxx = -1

        for num in count:
            if count[num] == 1 and num > maxx:
                maxx = num
        return maxx


        