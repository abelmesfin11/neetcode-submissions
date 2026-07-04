# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = float('inf')
        ans = 0

        def dfs(node):
            nonlocal curr, ans
            if not node:
                return
            
            diff = abs(node.val - target)

            if diff < curr:
                curr = diff
                ans = node.val

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans

        

    


        