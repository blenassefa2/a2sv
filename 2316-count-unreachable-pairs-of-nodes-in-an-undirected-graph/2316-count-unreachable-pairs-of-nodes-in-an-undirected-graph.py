class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        
        n
        n * n-1
        
        [0,1] == [1,0]
        total_connected = 0
        
        [0,2,4,5] = 4 *3 = 12//2  = 6, total += 6
        [1,6] = 2 *1 = 2 = 1, total += 1
        [3] =  1 * 0 = 0 = 0, total += 0
        
        
        
        function magic(node, visited):
            if node is in visited:
                return 0
                
            node --> add visited
            l = 1
            for i, j in edges:
                if i == node:
                    l += magic(j, visited )
                if j == node:
                    l += magic(i, visited )
                    
            return l
        
        v = {}
        total_connected = 0
        
        for i 0 ---> n:
            if i not in v:
                temp = magic(i,v)
                total_connected += ((temp * (temp -1))//2)
        
        
        
        
        total_comb = n *(n-1) = t/2 = 21
        
        total_not_connected = total_comb - total_connected
        
        return  total_not_connected  
        
        time complexity =  O(n)
        space complexity =  O(n)
        """
        
        parents = defaultdict(list)
        for i, j in edges:
            parents[i].append(j)
            parents[j].append(i)
        
        def magic(node, visited):
            if node in visited:
                return 0
            visited.add(node)
            l = 1
            
            for child in parents[node]:
                
                l += magic(child, visited)
            
            return l  
        
        v = set()
        total_connected = 0
        
        for k in range(n):
            if k not in v:
                temp = magic(k,v)
                total_connected += ((temp * (temp -1))//2)
                
        total_comb = (n * (n-1))//2
        
        return total_comb - total_connected