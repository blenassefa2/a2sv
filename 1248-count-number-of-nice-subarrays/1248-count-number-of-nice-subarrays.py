class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        this is almost the same as the sub array with sum atleast k
        
        Thought Process:
        ----------------
        
        so wat we do is construct a prefix array of number of odds before the index i
        then we do sliding window on that prefix array
        what we are looking for is the arrays that have odd nums exactly k
        
        Algorithm:
        ----------
        
        construct prefix array
        create temp array
        
        final = 0
        last_total = 0
        iterate i 0 -> len(prefix array):
            current_total = 0
            if the current array is not empty and the count of odds from start to i >= k:
                increament current total by 1
                reduce size of array from left
        
            if current_total:
                last_total = current_total
            else:
                current_total += last_total
            
            final += current_total
        
        complexity:
        -----------
    
        Time, space = O(n), O(n)
                
        
        """   
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + (i%2))
        
        final, last_total = 0,0
        
        qu = deque([])
        for i in prefix:
            current = 0
            while qu and i - qu[0] >= k:
                current += 1
                qu.popleft()
            if current:
                last_total = current
            else:
                current = last_total
            final += current
            qu.append(i)
        
        return (final)   
            
            
            
        
        