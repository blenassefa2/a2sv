class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        brute force approach:
        --------------------
        
        calculate total_space
        decreament the guards and wall from total_space
        
        for each guard 
            calculate how long it can guard 
            then update total_guarded
            
        return final of total_space -total_guarded
        
        complexity:
        -----------
        
        Time complexity  = O(len(guards)*(n+m) )
        space complexity = O(n*m)
        
        """
        total_space = (n * m) - len(guards) - len(walls)
        w , g = set(), set()
        
        for wall in walls:
            w.add((wall[0], wall[1]))
        for wall in guards:
            g.add((wall[0], wall[1]))
        found  = set()
        
        
        for a,b in guards:
            
            
            
            for i in range(a+1, m):
                
                if (i,b) in w or (i,b) in g:
                    break
            
                found.add((i,b))
            for j in range(a-1,-1,-1):
                
                if (j,b) in w or (j,b) in g:
                    break
               
                found.add((j,b))
            for k in range(b+1, n):
                
                if (a,k) in w or (a,k) in g:
                    break
                
                found.add((a,k))
            for l in range(b-1,-1,-1):
                
                if (a,l) in w or (a,l) in g:
                    break
            
                found.add((a,l))
           
        return (total_space) - len(found)
        