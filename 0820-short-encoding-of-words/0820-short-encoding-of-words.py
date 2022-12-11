class Node:
    def __init__(self):
        self.children = defaultdict()
        
        
class Trie:
    def __init__(self):
        self.head = Node()
        
    def insert(self, word):
        current = self.head
        
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
           
            current = current.children[char]
        
    def notPrefix(self, word):
        current = self.head
        
        for char in word:
            if char not in current.children:
                return True
            current = current.children[char]
        
        return False
            
                
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x: -len(x))
        
        trie = Trie()
        
        
        
        totalLength = 0
        
        for word in words:
            if trie.notPrefix(word[::-1]):
                trie.insert(word[::-1])
                totalLength += len(word) + 1
        
        return totalLength
        
        
        
        