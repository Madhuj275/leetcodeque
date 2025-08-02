# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        st=[]
        st.append((root,float('-inf')))
        count=0

        while st:
            node, maxi= st.pop()
            if maxi <= node.val:
                count+=1
            
            if node.left:
                st.append((node.left,max(node.val,maxi)))
            
            if node.right:
                st.append((node.right,max(node.val,maxi)))
        
        return count
        