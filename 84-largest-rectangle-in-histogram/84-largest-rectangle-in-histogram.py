class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        use monotonic increasing stack to keep important heights
                     
        for example if you have 2, 8, 4
        after you discover 4 is not important any more
        
        when you reach this types of points you calculated the 
        maximum area this can make with the numbers behind them
        
                       

        when I try to generalize it using the blog I read
            ** It is a “range queries in an array” problem.(width)
            ** The minima/maxima element or the monotonic 
                order of elements in a range is useful to 
                get answer of every range query.(the minimum decides the area in a range of width)
            ** When a element is popped from the monotonic stack, 
                it will never be used again.(the ones that alter the monotonicity)
        
        """
        stack = []
        heights.append(0)
        marea = 0
        for i, val in enumerate(heights):
            
            while stack and heights[stack[-1]] > val:
                h = heights[stack.pop()]
                
                w = i if not stack else i - stack[-1] - 1
                
                marea = max(marea, w*h)
            
            
            stack.append(i)
        return marea