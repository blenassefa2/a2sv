"""
# Definition for Employee.
class Employee:
    def init(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(x,lst):
            if not lst:
                return x
            for i in range(len(lst)):
                for j in range(len(employees)):
                    if employees[j].id == lst[i]:
                        
                        lst2 = employees[j].subordinates
                        x += employees[j].importance
                        x = dfs(x,lst2)
            return x

                
                
        
        
        
        x = 0
        sum_ = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                x =  i
        
        lst = employees[x].subordinates
        sum_+= employees[x].importance
        return dfs(sum_,lst)