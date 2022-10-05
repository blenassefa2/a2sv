# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if not slow or not slow.next:
            return False
        while fast:
            
            fast = None if not fast.next else fast.next.next
            slow = slow.next
            if fast == slow:
                break
         
    
        return fast == slow
        
        