class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Thought process:
        
        the maximum repeated letter is the one that matters
        
        we want to get rid of these letters first(make sure they are adjusted properly)
        therefore every time we are building the final answer we must keep track of the current most frequent letter so that it is either the next letter  or  the letter after the second maximum 
        
        Time Cpmplexity:- O(nlog(n))
        space complexity:- O(n)
        
        """
        counts = [ [-1*v,k] for k, v in Counter(s).items()]
        
        heapify(counts)
        ans = ""
        while counts:
            c, l = heappop(counts)
            if ans and counts and ans[-1] == l:
                
                c2, l2 = heappop(counts)
                ans += l2
                if c2 +1 < 0:
                    heappush(counts, [c2+1,l2])
                heappush(counts, [c,l])
            else:
                if ans and ans[-1] == l:
                    return ""
                ans += l
                if c +1 < 0:
                    heappush(counts, [c+1,l])
                
        return "".join(ans) 
                
            
                
            
        
        
        
        
        