# Problem: Merge k Sorted Lists
# Difficulty: Unknown
# Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        merg_list = []
        for l in lists:
            while l:
                merg_list.append(l.val)
                l = l.next
        sorted_list = sorted(merg_list)
        dummy = ListNode(0)
        current = dummy
        for i in sorted_list:
            current.next = ListNode(i) 
            current = current.next

        return dummy.next