class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckies = []
        count = Counter(arr)
        maxNum = -float('inf')
        for num in count:
            if count[num] == num:
                luckies.append(num)
                if num > maxNum:
                    maxNum = num
        return maxNum if maxNum != -float('inf') else -1