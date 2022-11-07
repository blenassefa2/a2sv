class Node:
    def __init__(self,index=-1):
        self.children = defaultdict()
        self.index = index
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = Node()
       
    def insert(self, word, index):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(index)
            current = current.children[char]
        current.isEnd = True
    
    def searchPrefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return -1
            current = current.children[char]
        return current.index +1
    
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        trie = Trie()
        for index in range(len(sentence)):
            word = sentence[index]
            trie.insert(word, index)
        
        return trie.searchPrefix(searchWord)