# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxx = -float('inf')
        def dfs(node):
            if not node:
                return 0

            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            res = node.val + l + r
            self.maxx = max(self.maxx, res)

            return node.val + max(l, r)

        dfs(root)
        return self.maxx if self.maxx != -float('inf') else 0

        
        