class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        store = []
        result = []
        
        
        for char in counts:
            store.append((-counts[char], char))
            
        heapify(store)
        
        
        while store:
            first = heappop(store)
            second = None
            
            if result and result[-1] == first[1]:
                if not store:
                    return ""
                second = heappop(store)
                heappush(store,first)
                first = second
                
            result.append(first[1])
            
            if first[0] + 1 < 0:
                heappush(store, (first[0] + 1, first[1]))
                
        return "".join(result)
                
                
            
            
            
            
            
        