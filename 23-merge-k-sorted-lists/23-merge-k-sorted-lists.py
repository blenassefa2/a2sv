# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

       
       
        ans = ListNode()
        tmp = ans
        while True:
            lis = []
            x = 1000000000
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val == x:
                        lis.append(i)
                    elif lists[i].val < x:
                        lis = [i]
                        x = lists[i].val
                        
          
            for j in lis:
                lists[j] = lists[j].next
                tmp.next = ListNode(x,None)
                tmp = tmp.next
            if not lis:
                break
            
        return ans.next
        