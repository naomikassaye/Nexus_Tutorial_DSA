# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, pt1: Optional[ListNode], pt2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        temp = merged
        while pt1 and pt2:
            if pt1.val < pt2.val:
                temp.next = pt1
                pt1 = pt1.next
            else:
                temp.next = pt2
                pt2 = pt2.next
            temp = temp.next
        if pt1:
            temp.next = pt1
        if pt2:
            temp.next = pt2
        return merged.next
