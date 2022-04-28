class Node:
    def __init__(self):
        self.children = [None]*26
        self.end = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        
        for val in word:
            index = ord(val) - 97
            if current.children[index] == None:
                current.children[index] = Node()
            current = current.children[index]
        current.end = True
            

    def search(self, word: str) -> bool:
        current = self.root
        for val in word:
            index = ord(val) - 97
            if current.children[index] == None:
                return False
            current = current.children[index]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for val in prefix:
            index = ord(val) - 97
            if current.children[index] == None:
                return False
            current = current.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)