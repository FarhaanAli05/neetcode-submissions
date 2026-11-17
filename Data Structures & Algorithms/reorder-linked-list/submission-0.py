# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        mid = end = head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2 = mid.next
        mid.next = None
        # reverse part 2
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev
        # intermix part 1 and part 2 nodes
        while p2:
            p1next = head.next
            head.next = p2
            p2next = p2.next
            p2.next = p1next
            head = p1next
            p2 = p2next