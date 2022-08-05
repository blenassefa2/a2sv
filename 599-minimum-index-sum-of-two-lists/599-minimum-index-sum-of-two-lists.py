class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = defaultdict(list)
        
        for i in range(len(list1)):
            map1[list1  [i]].append(i)
        
        for j in range(len(list2)):
            map1[list2[j]].append(j)
            
        ans = 100000000
        
        for j in map1:
            if len(map1[j]) == 2:
                ans = min(ans, sum(map1[j]))
            else:
                map1[j] = []
                
        final = []
        
        for i in map1:
            if sum(map1[i]) == ans and len(map1[i]) == 2:
                final.append(list1[map1[i][0]])
                
        return final
            