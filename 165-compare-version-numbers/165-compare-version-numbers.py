class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        
       
        for i in range(len(v1)):
           
            v1[i]= int(v1[i])
           
        for j in range(len(v2)):
            
            v2[j]= int(v2[j])
            
        x,y = 0,0
        while x < len(v1) or y < len(v2):
            if x >= len(v1) and y < len(v2):
                v1.append(0)
            if x < len(v1) and y >= len(v2):
                v2.append(0)
         
            if v1[x] > v2[y]:
                return 1
            elif v1[x] < v2[y]:
                return -1
            
            x += 1
            y += 1
        return 0
                
            
            