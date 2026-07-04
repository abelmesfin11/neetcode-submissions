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

            if diff < curr or (diff == curr and node.val < ans):
                curr = diff
                ans = node.val

            if target > node.val:
                dfs(node.right)
            elif target < node.val:
                dfs(node.left)
    
        dfs(root)
        return ans

        

    


        