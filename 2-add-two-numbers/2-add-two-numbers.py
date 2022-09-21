# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recurse(n1,n2,carry):
            if not n1 and not n2:
                return None if not carry else ListNode(carry)
            sum_ = carry
            if n1:
                sum_ += n1.val
                n1 = n1.next
            if n2:
                sum_ += n2.val
                n2 = n2.next
            
            carry = 0
            if sum_ >= 10:
                carry = 1
                sum_ = sum_%10
            the_rest = recurse(n1,n2,carry)
            return ListNode(sum_, the_rest)
        return recurse(l1,l2,0)