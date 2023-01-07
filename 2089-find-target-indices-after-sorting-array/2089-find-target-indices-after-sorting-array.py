class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """ To have TC of O(1) I will use count sort SS of O(n)"""
        
        # initialize the necessary variables
        counts = [0]* (max(nums) + 1)
        answer = []
        index = 0
        countsIndex = 0
        
       
        # fill the counts array
        for i in nums:
            counts[i] += 1
            
        # update nums to its sorted version inplace
        while countsIndex < len(counts):
            if counts[countsIndex] > 0:
                nums[index] = countsIndex
                
                # update the answer
                if nums[index] == target:
                    answer.append(index)
                
                #update the indecies
                counts[countsIndex] -= 1
                index += 1
            
            if counts[countsIndex] == 0:
                countsIndex += 1
     
        return answer
        
        