# Problem: Construct Binary Tree from Inorder and Postorder Traversal
# Difficulty: Unknown
# Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        ino = {}
        for key, value in enumerate(inorder):
            ino[value] = key
        
        def helper(left, right):
            if left > right: return None
            
            root_val = postorder.pop()
            root_index_inorder = ino[root_val]
            root = TreeNode(root_val,None, None)
            root.right = helper(root_index_inorder+1, right)
            root.left = helper(left, root_index_inorder-1)
            return root

        return helper(0, len(inorder)-1)
        