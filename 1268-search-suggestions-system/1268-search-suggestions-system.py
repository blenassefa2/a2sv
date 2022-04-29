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
            

    def choose(self, word: str, n, di):
        if word in di:
            return di[word]
        if n == 3:
            return []
        current = self.root
        a = ""
        for val in word:
            index = ord(val) - 97
            if current.children[index]:
                a += chr(index + 97)
                current = current.children[index]
        
        if a != word:
            return []
        
        lis = []

        if current.end == True:
            n += 1
            lis.append(word)
        for i in range(26):
            ch = word
            if len(lis) < 3:
                if current.children[i]:
                    ch += chr(i + 97)
                    y = self.choose(ch,n,di)
                    j = 0
                    while len(lis) < 3 and j < len(y):
                        lis.append(y[j])
                        j += 1
        di[word] = lis
        return lis
                

        
        
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        collect = Trie()
        for i in products:
            collect.insert(i)
        ans = []
        s = ""
        a = defaultdict(list)
        for j in range(len(searchWord)):
            s += searchWord[j]
            ans.append(collect.choose(s,0,a))
        return ans
            
            
            