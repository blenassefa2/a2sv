class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = defaultdict(lambda:1001)
        
        for i in range(len(arr2)):
            index[arr2[i]] = i
            
        
        arr1.sort(key = lambda x: (index[x], x) )
        
        return arr1