# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = None
        while head != None:
            cur = ListNode()
            cur.val = head.val
            cur.next = prev
            prev = cur
            head = head.next
            
        return cur