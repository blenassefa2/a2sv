class Solution:
    def trap(self, height: List[int]) -> int:
        """
         [0,1,0,2,1,0,1,3,2,1,2,1]
         
         this one uses monotonic stack to keep track of a left border
         once it reaches a potential right border 
            it pops all the bottom blocks
            and add what ever water they held
            decrement the height that has already been covered by bottom blocks
        """
        
        total = 0
        
        stack = []
        
        for i, val in enumerate(height):
            
            while stack and height[stack[-1]] <= val:
                index = stack.pop()
                
                if not stack:
                    break
                
                h = min(height[stack[-1]], val) - height[index]
                w = i - stack[-1] - 1
                total += h*w
            
            stack.append(i)
            
        return total