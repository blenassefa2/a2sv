class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        for a sub array to be divisible by k 
            we want its sum to have a remainder of 0 when divided by k
        
        if at index i the running sum has x remainder when divided by k and
        
        if at any index j >i the running sum has x remainder when divided by k
        
        then  the sum from i to j ==> sum[j] - sum[i]
                                  ==>  (k*n + x) -(k*m +x)
                                  ==> k*n +x -k*m - x 
                                  ==> k *(n-m)
                                  ==> k*c
                                  proving the interval from i to j is divisible by k
        thus for every x (remainder of running sum at index i and k)
        x.count combination 2 is the number of subarrays that are created by the i's
        
        if x == 0 then (x.count+1) combination 2 because the running summs are also divisible by k and counted as subarray
        
        
        """
        count = defaultdict(int)
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            count[nums[i]%k] += 1
        count[nums[0]%k] += 1
        
        total = 0
        for c in count:
            a =count[c]
            if c == 0:
                a += 1
            total += (a*(a -1))//2
        
        return total
                
            
            
       