# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)
    def helper(self, root, targetSum, result): 
        if root is None and targetSum == 0: 
            return False
        elif root is None: 
            return False
            
        result += root.val
        if root.left == None and root.right == None:
            if result == targetSum:
                return True
            else:
                return False        
        
        l_tree = self.helper(root.left, targetSum, result)
        r_tree = self.helper(root.right, targetSum, result)

        if l_tree or r_tree == True:
            return True
        elif l_tree == False and r_tree == False:
            return False 