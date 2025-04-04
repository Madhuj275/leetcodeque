# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):

        def dfs(node, depth):
            if not node:
                return (None, depth)
            
            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return (left_lca, left_depth)
            elif right_depth > left_depth:
                return (right_lca, right_depth)
            else:
                return (node, left_depth)

        return dfs(root, 0)[0]
        