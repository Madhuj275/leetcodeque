# Problem: Find Elements in a Contaminated Binary Tree
# Difficulty: Unknown
# Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: TreeNode):
        self.node_values = set()
        if root:
            root.val = 0
            self.node_values.add(0)
            self.recover_binary_tree(root.left, 1)
            self.recover_binary_tree(root.right, 2)

    def recover_binary_tree(self, curr: TreeNode, val: int):
        if not curr:
            return

        curr.val = val
        self.node_values.add(val)
        self.recover_binary_tree(curr.left, 2 * val + 1)
        self.recover_binary_tree(curr.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.node_values
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)