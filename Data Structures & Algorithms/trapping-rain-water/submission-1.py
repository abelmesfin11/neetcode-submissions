class Solution:
    def trap(self, height: List[int]) -> int:
        """
        idea: at a position i, how do we find the max water trapped?
        ans: min(max(left), max(right)) - height[i]
        """ 
        n = len(height)
        leftMax = 0
        rightMax = 0
        left = [0] * n
        right = [0] * n

        for i in range(n):
            j = - i - 1
            left[i] = max(leftMax, height[i])
            leftMax = max(leftMax, height[i])
            right[j] = max(rightMax, height[j])
            rightMax = max(rightMax, height[j])

        res = 0
        for i in range(n):
            potential = min(left[i], right[i]) 
            res += max(0, potential - height[i])
        return res







