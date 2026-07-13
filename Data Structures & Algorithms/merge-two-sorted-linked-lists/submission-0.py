# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res = dummy = ListNode()
        while curr1 and curr2:
            if curr1 and curr2 and curr1.val < curr2.val:
                dummy.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                dummy.next = ListNode(curr2.val)
                curr2 = curr2.next
            dummy = dummy.next

        if curr1:
            dummy.next = curr1
            

        if curr2:
            dummy.next = curr2

        return res.next
        