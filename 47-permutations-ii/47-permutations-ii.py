class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = [""]
       
        m = [str(x) for x in range(len(nums))]
        m ="".join(m)
        
        n = len(nums)
    
        for i in range(n):
            a= []
            for result in results:
                for d in m:
                    if result:
                         if d not in result:
                            
                            a.append(result+ d) 
                    else:
                        a.append(d)
            
            results = a
        final = set()
        for result in results:
            x = ()
            for k in result:
                x += (nums[int(k)],)
            if x not in final:
                final.add(x)
                            
            
        return(list(final))