# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
    
        self.ans = False
        def dfs(node, curr):
            if not node:
                return

            if not node.left and not node.right:
                if curr == targetSum:
                    self.ans = True
        
            if node.left:
                dfs(node.left, curr + node.left.val)
            if node.right:
                dfs(node.right, curr + node.right.val)

        dfs(root, root.val)
        return self.ans

            
        