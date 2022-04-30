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
class Solution:
    def longestWord(self, words: List[str]) -> str:
        dictionary = Trie()
        words.sort(key = lambda x: (-1*len(x),x))
        
        for i in words:
            dictionary.insert(i)
        
        large = -10
        word = ""
    
        for i in words:
            is_word = True
            c = i[0]
            for j in range(1,len(i)):
                if dictionary.search(c):
                    c += i[j]
                else:
                    is_word = False
                    break
            if len(i) > large and is_word:
                word = i
                large = len(i)
        return (word)