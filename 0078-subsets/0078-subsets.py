class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.final = set()
        def recurse(index, path):
            if index >= len(nums):
                self.final.add(tuple(sorted(path)))
                return 
            
            p1 = [i for i in path]
            p2 = [i for i in path]
            p2.append(nums[index])
            recurse(index + 1, p1)
 
            recurse(index+ 1, p2)
            
            return 
        
        recurse(0, set())
        return self.final
            