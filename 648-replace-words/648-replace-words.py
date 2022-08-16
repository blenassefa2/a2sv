class Node:
    def __init__(self):
        self.children = defaultdict()
        self.endMark = False 
    
class Trie:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        current = self.trie
        for w in word:
            if w not in current.children:
                current.children[w] = Node()
            if current.endMark:
                return
            current = current.children[w]
        current.endMark = True

    def search(self, word: str) -> str:
        current = self.trie
        for i in range(len(word)):
            
            if current.endMark:
                return word[:i]
            if word[i] not in current.children:
                return word
            current = current.children[word[i]]
        return word

    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        sent = sentence.split(" ")
        
        for s in range(len(sent)):
            sent[s] = trie.search(sent[s])
            
        return " ".join(sent)
        
        
        