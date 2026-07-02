"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return 

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == p.val or node.val == q.val:
                return node

            if left and right:
                return node

            return left if left else right

        return dfs(root)