class Solution:
    def search(self, array, key):
        
        
        left = 0
        right = len(array) -1
        
        best = len(array)
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if key < array[mid]:
                best = mid
                right = mid - 1
            
            else:
                left = mid + 1
        return len(array) - best
                
    def f(self,word):
        # returns frequency of the lexicographically smollest char
        freq = Counter(word)
        ans = word[0]
        
        for i in range(len(word)):
            ans = min(ans, word[i])
        
        return freq[ans]
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # declare variables
        wordValues = []
        answer = []
        
        # build values arrays
       
        for word in words:
            wordValues.append(self.f(word))
            
        wordValues.sort()
        
        
        # binary search and populate answer
        for query in queries:
            value = self.f(query)
            
            answer.append(self.search(wordValues, value))
        
        
        return answer