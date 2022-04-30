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
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        words.sort()
        trie = Trie()
        
        
        for i in words:
            if trie.search(i):
                counts[i] += 1
            else:
                counts[i] = 0
            trie.insert(i)
            
        ans = [(x,-1*counts[x]) for x in counts]
        ans.sort(key = lambda a:(a[1],a[0]))
        ans = deque(ans)
        
        final = []
        while k:
            final.append(ans[0][0])
            ans.popleft()
            k -= 1
        return(final)
        
       

        
        