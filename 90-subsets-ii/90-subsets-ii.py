class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        
        def recurse(i,path):
            if i >= len(nums):
                self.ans.add(tuple(sorted(path)))
                return
            
            recurse(i+1,path)
            path += (nums[i],)
            recurse(i+1, path)
        recurse(0, ())
        return self.ans