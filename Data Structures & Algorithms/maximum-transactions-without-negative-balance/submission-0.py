class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        cur = 0
        ans = []

        for num in transactions:
            cur += num
            if cur < 0:
                cur -= num
                continue
            else:
                ans.append(num)

        return len(ans)

        