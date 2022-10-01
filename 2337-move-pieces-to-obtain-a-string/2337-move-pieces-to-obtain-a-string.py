class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        if the counter of the start and the target are not the same then no need to bother
        
        if that is not the case we can start to build target from start
        
        I am going to pop from the right therefore if the two aren't matching
            we have two types of not matching:
                ones that will never work: return False
                    t -> L s -> _
                    t -> R s ->L
                    t -> L s -> R
                    t -> _ s -> R
                ones that might work
                    t -> R s ->_
                        go back until you find R:
                             if you find L: return False
                             if you find R : swap with the last
                    t -> _ s ->L
                        go back until you find _:
                             if you find R: return False
                             if you find _ : swap with the last
                    
        """
        
        if Counter(start) != Counter(target):
            return False
        work = lambda s,t: s == t or (t == "R" and s=="_") or (t =="_" and s=="L")
        start = list(start)
        target = list(target)
        k,g = len(start)-1,len(target)-1
        while start and target:
            if not work(start[-1], target[-1]):
                return False
            s,t = start.pop(), target.pop()
            if s == t:
                continue
            lookFor,abort = "R", "L"
            i = min(k,len(start)-1)
            if s == "L":
                i = min(g,len(start)-1)
                lookFor,abort = "_", "R"
            
            while i >= 0:
                if start[i] == lookFor:
                    if s == "L":
                        g = i
                    else:
                        k = i
                    start[i] = s
                    break
                if start[i] == abort:
                    return False
                i -= 1
        return True
            
        
        