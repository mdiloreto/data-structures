# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
       1
   2       2
 3   4   4   3
9 8 8 7 7 8 8 9
    """
    def isSymmetric(self, root) -> bool:
        return self.findsimetry(root.left, root.right)

    def findsimetry(self, l, r):
        if not l and not r: 
            return True 
        if not l or not r: 
            return False
        return l.val == r.val and self.findsimetry(l.left, r.right) and self.findsimetry(l.right, r.left)
        # if l and r and l.val == r.val:
        #     left = self.findsimetry(l.left, r.right)
        #     right = self.findsimetry(l.right, r.left)
        #     return left and right       


 