class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckies = []
        count = Counter(arr)
        for num in count:
            if count[num] == num:
                luckies.append(num)
        return max(luckies) if luckies else -1