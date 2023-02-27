# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None
        rabit,tortoise = head, head
        
        # phase 1
        while rabit and rabit.next:
            
            rabit = rabit.next.next
            tortoise = tortoise.next
            if rabit == tortoise:
                
                break
        if not rabit:
            return  None
        
        rabit = head
        #phase 2
        while rabit and tortoise:
            if rabit == tortoise:
                return rabit
            rabit = rabit.next
            tortoise = tortoise.next
            
        return None