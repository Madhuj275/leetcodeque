# Problem: Remove Duplicates from Sorted List II
# Difficulty: Unknown
# Solution:

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur_val = head.val
        if head.next and head.next.val == cur_val:
            while head and head.val == cur_val:
                head = head.next 
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head