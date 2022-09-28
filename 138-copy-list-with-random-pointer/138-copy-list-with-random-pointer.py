"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
    
        temp = head
        
        while temp:
            temp.next = Node(temp.val,temp.next)
            temp = temp.next.next
        
        temp = head
        
        while temp and temp.next:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        temp = head.next
        while temp.next:
            temp.next = temp.next.next
            temp = temp.next            
        return head.next