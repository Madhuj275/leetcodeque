# Problem: Reverse Nodes in k-Group
# Difficulty: Unknown
# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        curr=head
        while curr:
            l.append(curr.val)
            curr=curr.next
        for i in range(0,len(l)-k+1,k):
            l[i:i+k]=reversed(l[i:i+k])
        dummy=ListNode()
        curr=dummy
        for val in l:
            curr.next=ListNode(val)
            curr=curr.next
        return dummy.next
        
            