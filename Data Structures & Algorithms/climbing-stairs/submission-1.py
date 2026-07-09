class Solution:
    def climbStairs(self, n: int) -> int:
        def memo(n, memo_dict):
            if n <= 2:
                return n

            if n in memo_dict:
                return memo_dict[n]

            memo_dict[n] = memo(n-1, memo_dict) + memo(n-2, memo_dict)
            return memo_dict[n] 

        return memo(n, {})
            

        