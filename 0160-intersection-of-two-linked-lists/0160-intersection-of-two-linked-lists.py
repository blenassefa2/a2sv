# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  
        
        tailA = []
        tailB = []
        
        while headA:
            tailA.append(headA)
            headA = headA.next
        while headB:
            tailB.append(headB)
            headB = headB.next
            
        answer = None
        while tailA and tailB:
            if tailA[-1] != tailB[-1]:
                return answer
            answer = tailA.pop()
            tailB.pop()
        return answer