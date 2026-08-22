# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(0, next=head)
        prev = d
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next

        return d.next


        
            
            

            
        
        