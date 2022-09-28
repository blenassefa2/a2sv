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
        temp = head
        o_n = defaultdict()
        
        while temp:
            o_n[temp] = Node(temp.val)
            temp = temp.next
        
        temp = None
        t2= head
        while head:
            n,r = head.next, head.random
            temp = o_n[head]
            
            temp.next = o_n[head.next] if head.next else None
            temp.random = o_n[head.random] if head.random else None
            head = head.next
            temp = temp.next
        return o_n[t2] if t2 else None