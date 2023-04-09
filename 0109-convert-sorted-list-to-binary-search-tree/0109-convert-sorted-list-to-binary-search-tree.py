# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        middle = head
        end = head
        
        while end and end.next:
            lst = middle
            middle = middle.next
            end = end.next.next
        root = middle.val
        lst.next = None
        right= self.sortedListToBST(middle.next)
        
        left = self.sortedListToBST(head)
        return TreeNode(root, left, right)
        