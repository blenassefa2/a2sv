class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = set()
        def recurse(i, current):
            if i >= len(nums):
                final.add(tuple(current))
                return



            add = recurse(i + 1, [nums[i]]  + current)
            noAdd = recurse(i + 1, current)
            
            return
        
        for j in range(len(nums)):
            recurse(j,[])
        return final
    
 
            
                