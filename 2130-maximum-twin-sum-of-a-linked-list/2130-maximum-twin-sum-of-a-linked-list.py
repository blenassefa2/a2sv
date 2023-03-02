# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def rev(node):
            prev = None
            current = node
            while current :
                
                tp = current.next
                current.next = prev
                prev = current
                current = tp
           
            return  prev
        
        
        half = head
        end = head
        bHalf = half
        
        while end and end.next:
            bHalf = half
            half = half.next
            end = end.next.next
            
        
        bHalf.next = rev(half)
        half = head
        end = head
        
        while end and end.next:
            half = half.next
            end = end.next.next
            
        ret = -1
        left = head
        while half:
            ret = max(ret, left.val+half.val)
            half = half.next
            left = left.next
        return ret