class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=j=0
        if(len(nums)<3):
            return len(nums);
        s=2
        for f in range(2,len(nums)):
            if nums[f]!=nums[s-2]:
                nums[s]=nums[f]
                s+=1
                
        return s