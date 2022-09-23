class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
       
        
            
        lable =[]
        coll = set()
        for l,r in intervals:
            if l == r:
                coll.add(l)
            lable.append([l,'b'])
            lable.append([r, 'e'])
        
        lable.sort()
        final = []
        line = [0]* len(lable)
        
        
        i = 0
        for v,l in  lable:
            if l == 'b':
                line[i] += 1
            else: 
                line[i] -= 1
            i += 1
        for i in range(1,len(line)):
            line[i] += line[i-1] 
        i = 0
        while i < len(line):
            if line[i] > 0:
                a = lable[i][0]
                while  line[i] > 0:
                    i += 1
                final.append([a,lable[i][0]])
            else:
                if i in coll:
                    final.append([lable[i][0],lable[i]])
            i += 1
        
        
        return final