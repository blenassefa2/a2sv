class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # initialize variables
        contentKey = defaultdict(list)
        
        
        # distribute file path
        for i in range(len(paths)):
            files = paths[i].split(" ")
            
            for j in range(1,len(files)):
                file = files[j]
                
                content= file.split("(")
                
                contentKey[content[1][:-1]].append(files[0] + "/" + content[0])
        
        # return the values
        answer = []
        for i in contentKey.values():
            if len(i) > 1:
                answer.append(i)
        return answer