class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # initialize variables
        counts = Counter(barcodes)
        store = []
        result = []
        
        
        # populate store
        for code in counts:
            store.append((-counts[code], code))
        
        heapify(store)
        
        while store:
            first = heappop(store)
            second = None
            
            # make sure adjacents are different
            if result and result[-1] == first[1]:
                second = heappop(store)
                heappush(store, first)
                first = second
                
            # update result and store
            result.append(first[1])
            
            if first[0] + 1 < 0:
                heappush(store, (first[0] + 1, first[1]))
                
        return result
            
                
        
    