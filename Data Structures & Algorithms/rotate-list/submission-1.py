# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next

        k %= total 

        if k == 0:
            return head
         
        # disconnect
        c = cur = head
        for i in range(total - k - 1):
            cur = cur.next

        tmp = cur.next
        cur.next = None

        tail = tmp
        for i in range(k-1):
            tail = tail.next

        tail.next = c
        return tmp



        
            

        