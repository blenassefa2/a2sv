# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        full rotation
        
        rotate all values after k%length values to original
        """
        if not head: return head
        
        def rotate(curr, prev):
            length = 0
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

                length += 1
        
            return length, prev
        #full rotation
        length, head = rotate(head, None)
             
        
        k = k % length
        x = k
        last = head
        bef = last
        while x > 0:
            bef = last
            last = last.next
            x -=1
        
        length, last = rotate(last, None)
        if k == 0: return last
        bef.next = None
        length, head = rotate(head, None)
        bef = head
        while bef and bef.next:
            bef = bef.next
        bef.next = last
       
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        