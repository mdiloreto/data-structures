# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    4
   7 2
 6 9 1 3
  
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            temp_root = root.left
            root.left = root.right
            root.right = temp_root
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
        return root