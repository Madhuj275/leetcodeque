# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node,tsum):
            if not node:
                return False
            tsum+=node.val
            if not node.left and not node.right:
                return tsum== targetSum
            
            return helper(node.left,tsum) or helper(node.right,tsum)
        
        return helper(root,0)
                

        

        