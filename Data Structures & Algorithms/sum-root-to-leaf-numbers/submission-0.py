# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = []
        def dfs(node, curr):
            if not node:
                return 0
        
            curr = 10 * curr + node.val

            if not node.left and not node.right:
                self.res.append(curr)

            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            
            return left + right

        dfs(root, 0)

        return sum(self.res)