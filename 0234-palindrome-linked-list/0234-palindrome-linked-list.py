# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle element
        middle = head
        end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next
        
        # reverse all the parts
        prev = None
        current = middle
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        start = head
        
        while start and prev:
            if start.val != prev.val:
                return False
            
            start = start.next
            prev = prev.next
        
        return True