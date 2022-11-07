class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Handle the edge cases
        if len(p) > len(s):
            return []
        
        # initialize variables
        requiredState = Counter(p)
        currentState = defaultdict(int)
        
        leftPointer = 0
        rightPointer = 0
        
        finalArray = []
        
        final = 0
        current = 0
        for i in p:
            final |= 1<<(ord(i) - ord("a"))
    
        # slide the window keeping track of start index of valid anagrams
        while rightPointer < len(s):
            
            if s[rightPointer] not in requiredState:
                rightPointer += 1
                leftPointer  = rightPointer
                currentState = defaultdict(int)
                current = 0
               
            else:
                if currentState[s[rightPointer]] < requiredState[s[rightPointer]]:
                    currentState[s[rightPointer]] += 1
                    if currentState[s[rightPointer]]== requiredState[s[rightPointer]]:
                        current |= (1<<(ord(s[rightPointer]) -ord("a")))
                    
                    rightPointer += 1
                        
                    
                elif currentState[s[rightPointer]] >= requiredState[s[rightPointer]]:
                
                    if current& (1<<(ord(s[leftPointer]) -ord("a"))) > 0:
                        current ^= (1<<(ord(s[leftPointer]) -ord("a")))
                        
                    currentState[s[leftPointer]] -= 1
                    leftPointer += 1
            if current == final:
                finalArray.append(leftPointer)
                
                
                
        
                 
           
            
        return finalArray