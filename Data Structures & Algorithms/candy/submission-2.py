class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        # left to right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = 1 + res[i-1]


        # right to left
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                res[j] = max(res[j], 1 + res[j+1])


        return sum(res)
        