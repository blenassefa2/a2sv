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
            current = current.children[w]
        current.endMark = True

    def search(self, word: str, prefix=False) -> bool:
        current = self.trie
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
            
        return prefix or current.endMark

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix,True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)