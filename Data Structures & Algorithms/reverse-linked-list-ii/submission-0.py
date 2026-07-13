# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = ListNode(0, head)
        
        prev = curr
        for i in range(left - 1):
            prev = prev.next

        left_node = prev.next

        last = curr
        for i in range(right):
            last = last.next

        
        remainLast = last.next
        last.next = None


        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        rev = reverse(left_node)

        prev.next = rev
        left_node.next = remainLast

        return curr.next








