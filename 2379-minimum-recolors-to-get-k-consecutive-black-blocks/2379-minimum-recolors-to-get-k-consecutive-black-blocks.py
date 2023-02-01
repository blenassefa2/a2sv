class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        intuition:
            we are going to check all of the possible consequative k blocks
            
            while we check
                we calculate amount of black needed to make the consecutive valid
                store the value if it is minimum than what we have seen before
        
        Basically use: fixed sliding window of size k
        
        Time complexity: O(n)
        space complexity: O(1)
        """
        
        # initialize variables
        minimumOperations = len(blocks)
        blackBlocks = 0
        leftPointer = 0
        rightPointer = 0
        
        
        # iterate until our window right is equal to array's end
        while rightPointer < len(blocks):
            
            
            # increase window size until it is == k
            while rightPointer < len(blocks) and rightPointer - leftPointer < k:
                
                blackBlocks += (blocks[rightPointer] == "B" )
                rightPointer += 1
            
            # if we have correct window size update optimum operations and  go to next window
            if rightPointer - leftPointer == k:
                    
                minimumOperations = min(minimumOperations, k - blackBlocks)
                blackBlocks -= (blocks[leftPointer] == "B")
                leftPointer += 1
                    
            
        return minimumOperations
                
        
        