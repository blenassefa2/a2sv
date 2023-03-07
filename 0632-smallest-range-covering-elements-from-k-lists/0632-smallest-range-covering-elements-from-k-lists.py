class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        for this question a dynamic size sliding window
        
        so first we tuple up the values with the index of the list they are part of
        
        then we broaden the the window to the right 
            until our window has values that are part of all lists
        
        then we narrow the window from the left 
            until the window doesn't have values that are part of all lists
        
        time complexity: O(n) where n is the sum of all elements in the lists
        space complexity: O(k) where k is the number of lists inside nums
        """
        # initialize variables
        left = 0
        right = 0
        found = set()
        vals = []
        answer = [-100000,1000000 ]
        count = defaultdict(int)
        
        # create the sorted array
        for index in range(len(nums)):
            for val in nums[index]:
                vals.append([val, index])
       
        
        vals.sort()
        
        while right < len(vals):
            
            while right < len(vals) and len(found) < len(nums):
                found.add(vals[right][1])
                count[vals[right][1]] += 1
                right += 1
            
            
            while left < right and len(found) == len(nums):
                answer = min(answer, [vals[left][0], vals[right-1][0]], key = lambda x: (x[1] - x[0], x[0]) )
                count[vals[left][1]] -= 1
                if not count[vals[left][1]]:
                    found.remove(vals[left][1])
                left += 1
        
        return answer