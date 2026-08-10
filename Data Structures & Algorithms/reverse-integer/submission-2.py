class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1
        reversedd = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            last = x % 10
            # overflow
            if reversedd > MAX // 10 or (reversedd == MAX // 10 and last > MAX % 10):
                return 0
            reversedd = reversedd * 10 + last
            x = int(x / 10)
        return sign * reversedd