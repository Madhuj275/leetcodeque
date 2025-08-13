# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def left_sub(node, max_val):
            if node is None:
                return True
            if node.val >= max_val:
                return False
            return left_sub(node.left, max_val) and left_sub(node.right, max_val)

        def right_sub(node, min_val):
            if node is None:
                return True
            if node.val <= min_val:
                return False
            return right_sub(node.left, min_val) and right_sub(node.right, min_val)

        def is_valid(node):
            if node is None:
                return True
            if not left_sub(node.left, node.val):
                return False
            if not right_sub(node.right, node.val):
                return False
            return is_valid(node.left) and is_valid(node.right)

        return is_valid(root)
        