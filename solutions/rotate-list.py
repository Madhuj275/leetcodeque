# Problem: Rotate List
# Difficulty: Unknown
# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        l=1
        curr=head
        while curr.next:
            curr=curr.next
            l+=1
        r=k%l
        k=l-r
        curr.next=head
        while k>0:
            curr=curr.next
            k-=1
        head=curr.next
        curr.next = None
        return head
        