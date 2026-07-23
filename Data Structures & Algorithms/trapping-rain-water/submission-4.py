class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = right_max = 0
        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(n):
            j = -1-i
            maxLeft[i] = left_max
            maxRight[j] = right_max
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
        
        ans = 0
        for i in range(n):
            pot = min(maxLeft[i], maxRight[i])
            ans += max(0, pot - height[i])
        
        return ans





        