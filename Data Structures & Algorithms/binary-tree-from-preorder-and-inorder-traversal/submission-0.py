# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        left = inorder[:idx]
        right = inorder[idx+1:]
        preorder.pop(0)

        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)

        return root