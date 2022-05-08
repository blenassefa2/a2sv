# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.li = deque([])
        
        def findall(y):
            x = y.getList()
            
            if not x:
                if y.isInteger():
                    self.li.append(y.getInteger())
            else:
                for x_ in x:
                    findall(x_)
        for i in nestedList:
            x = i.getList()
            if not x:
                if i.isInteger():
                    self.li.append(i.getInteger())
            else:
                for x_ in x:
                    findall(x_)
        print(self.li)
                    
    def next(self) -> int:
        return self.li.popleft()
    
    def hasNext(self) -> bool:
         return not (not self.li )

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())