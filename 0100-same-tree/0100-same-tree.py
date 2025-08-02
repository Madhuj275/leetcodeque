# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st=[]
        st.append((p,q))

        while st:
            a,b=st.pop()
            if a is None and b is None:
                continue
            if a is None or b is None:
                return False
            
            if a.val!=b.val:
                return False
            
            if a.left and b.left:
                st.append((a.left,b.left))
            elif a.left or b.left:  
                return False
            
            if a.right and b.right:
                st.append((a.right,b.right))
            elif a.right or b.right:  
                return False
                
        return True

        