class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0]
        
        for i in nums:
            runningSum.append(runningSum[-1] + i)
        return runningSum[1:]