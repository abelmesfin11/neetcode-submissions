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
            
            curr += node.val
            if not node.left and not node.right:
                if curr == targetSum:
                    self.ans = True
        
            dfs(node.left, curr)
            dfs(node.right, curr)

        dfs(root, 0)
        return self.ans

            
        