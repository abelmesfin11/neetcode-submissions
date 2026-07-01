# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return 

            if node.val == key:
                if not node.left and not node.right:
                    return
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    node.val = curr.val
                    node.right = dfs(node.right, curr.val)

            if key > node.val:
                node.right = dfs(node.right, key)
            else:
                node.left = dfs(node.left, key)
            return node

        return dfs(root, key)

        