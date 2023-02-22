class Solution:
    def binarySearch(self, num, arr):
        left = 0
        right = len(arr) -1
        best = right +1
        while left <= right:
            mid = (left + right)//2
            
            if arr[mid] > num:
                best = mid
                right = mid - 1
            else:
                left = mid +1
    
        return len(arr) - best 
            
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        [30, 20,30,40,40]
                   |
        20: 1
        30: 0,2
        40: 3,4
        
        1 + 2 + 0 + 0
        
        so we are going to have a dictionary of all remainders
        0,1, 2,3,4, .... 20....30...40...50..60
        
        then for each index we will search for the number of indexes that have remainders
        == 60 -  (time[i]%60)
        then sum up the result
        
        
        Time Complexity: O(nlogn)
        space Complexity: T(60) = O(1)
        """
        # initialize variable
        remainders = defaultdict(list)
        total = 0
        
        
        # populate the remainders dict
        for i in range(len(time)):
            remainders[time[i]%60].append(i)
        
       
        # for each time find its number of pairs
        for i in range(len(time)):
            pairs =  self.binarySearch(i, remainders[(60 - time[i]%60)%60])
        
            total +=pairs
        
        
        
        return total
        