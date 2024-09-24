# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.diameter(root, res)
        return res[0]
    def diameter(self, root, res):
        if root is None: 
            return 0

        left_depth = self.diameter(root.left, res) 
        right_depth = self.diameter(root.right, res) 

        res[0] = max(res[0], left_depth + right_depth)

        return 1 + max(left_depth, right_depth) 