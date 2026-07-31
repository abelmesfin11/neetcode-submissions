class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0: return False
        invert_map = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        rotated_number = []
        curr = n
        while curr:
            last = str(curr % 10)
            if last in invert_map:
                rotated_number.append(invert_map[last])
            else:
                return False
            curr = curr // 10
        num = "".join(rotated_number)
        return n != int(num)