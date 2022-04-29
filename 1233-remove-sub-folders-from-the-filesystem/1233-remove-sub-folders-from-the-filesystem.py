class Node:
    def __init__(self):
        self.children = defaultdict(str)
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        word = word.split("/")
        
        for val in word:
            
            if val not in current.children:
                current.children[val] = Node()
            elif current.children[val].end == True: 
                return
            current = current.children[val]
        current.end = True
            

    def search(self, word: str) -> bool:
        current = self.root
        word = word.split("/")
        for val in word:
            
            if val not in current.children:
                return False
            current = current.children[val]
        return current.end 

    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        main = Trie()
        
        folder.sort()
        ans = []
        for i in folder:
            
            main.insert(i)
                
        for j in folder:
            if main.search(j):
                ans.append(j)
   
        return ans
        
            
         
                
                
    