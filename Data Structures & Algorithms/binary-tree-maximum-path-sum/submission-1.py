# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        def dfs(node):
            if not node:
                return 0
            left = getMax(node.left)
            right = getMax(node.right)
            self.res = max(self.res, node.val + left + right)
            dfs(node.left)
            dfs(node.right)
       

        def getMax(node):
            if not node:
                return 0

            left = getMax(node.left)
            right = getMax(node.right)

            path = node.val + max(left, right)

            return max(0, path)

        dfs(root)
        return self.res

            









            
        

        