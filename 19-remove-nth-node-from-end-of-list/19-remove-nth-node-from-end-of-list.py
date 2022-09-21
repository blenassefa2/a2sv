# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head
        a = 0
        
        
        while p2.next:
            if a < n:
                p2 = p2.next   
                a += 1
            else:
                
                p1 = p1.next
                p2 = p2.next
               
        
        
        if a < n:
            head = p1.next
            return head
        p1.next = p1.next.next
        return head