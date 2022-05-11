class Solution:
    def countVowelStrings(self, n: int) -> int:
        results = ['']
        m = "aeiou"
    
        for i in range(n):
            a= []
            for result in results:
                for d in m:
                    if result:
                        if result[-1] <= d:
                            a.append(result + d) 
                    else:
                        a.append(d)
           
            results = a
                
                            
            
        return(len(results))