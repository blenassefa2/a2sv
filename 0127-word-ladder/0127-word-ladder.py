class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
            For this questionwe will treat the dictionary as a graph
            where the nodes are the words and
            an edge existes between two nodes iff the words differ only by one letter
            
            
            Do BFS on the created graph to find shortest distance between begin and end word
        """
        
        # initialize variables
        edges = defaultdict(set)
        qu = deque([beginWord])
        level = 1
        visited = set()
        
        # detect edge case and insert beginWord into dictionary
        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0
        if beginWord not in dictionary:
            wordList.append(beginWord)
        
        # construct the edges
        for i in range(len(wordList)):
            word1 = wordList[i]
            for index in range(len(word1)):
                for char in string.ascii_lowercase:
                    if char == word1[index]:
                        continue
                    word2 = [x for x in word1]
                    word2[index] = char
                    word2 = "".join(word2)
                    if word2 in dictionary:
                        edges[word1].add(word2)
                        edges[word2].add(word1)
            
        # perform the bfs
       
        while qu:
            N = len(qu)
           
            
            for _ in range(N):
                
                node = qu.popleft()
                
                if node == endWord:
                    return level
                
                if node in visited:
                    continue
                
                visited.add(node)
                
                while edges[node]:
                    qu.append(edges[node].pop())
                edges.pop(node)
            level += 1
        return 0