# Problem: Recover a Tree From Preorder Traversal
# Difficulty: Unknown
# Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        pos = [0]
        n = len(traversal)
        if n == 0:
            return None
        root_val = self._get_val(traversal, n, pos)
        root = TreeNode(root_val)
        self._build_tree(root, 1, traversal, n, pos)
        self._build_tree(root, 1, traversal, n, pos)
        return root
    
    def _get_val(self, traversal, n, pos):
        val = 0
        while pos[0] < n and traversal[pos[0]].isdigit():
            val = val * 10 + int(traversal[pos[0]])
            pos[0] += 1
        return val
    
    def _get_dash_len(self, traversal, n, pos):
        start = pos[0]
        while pos[0] < n and traversal[pos[0]] == '-':
            pos[0] += 1
        return pos[0] - start
    
    def _build_tree(self, curr, expected_dash_len, traversal, n, pos):
        if pos[0] >= n:
            return
        original_pos = pos[0]
        dash_len = self._get_dash_len(traversal, n, pos)
        if dash_len != expected_dash_len:
            pos[0] = original_pos
            return
        node_val = self._get_val(traversal, n, pos)
        new_node = TreeNode(node_val)
        if not curr.left:
            curr.left = new_node
        else:
            curr.right = new_node
        self._build_tree(new_node, expected_dash_len + 1, traversal, n, pos)
        self._build_tree(new_node, expected_dash_len + 1, traversal, n, pos)
        