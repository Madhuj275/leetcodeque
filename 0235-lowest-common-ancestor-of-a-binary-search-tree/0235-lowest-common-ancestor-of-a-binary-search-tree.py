class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            left_ans = helper(node.left)
            right_ans = helper(node.right)

            if left_ans and right_ans:
                return node

            return left_ans if left_ans else right_ans
        
        return helper(root)
