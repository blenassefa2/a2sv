class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0,len(intervals) - 1
        
        intervals.append(newInterval)
        intervals.sort()
        
        
        stack = []
        
        
        i = 0
        while i < len(intervals):
            if not stack:
                stack.append(intervals[i])
                i += 1
                continue
            
            last = stack.pop()
            
            if last[0] != intervals[i][0] and last[1] < intervals[i][0]:
                stack.append(last)
                stack.append(intervals[i])
            
            
            elif last[1] >= intervals[i][0] or last[0] == intervals[i][0]:
                last[1] = max(last[1], intervals[i][1])
                stack.append(last)
            
            
            i += 1
        return stack