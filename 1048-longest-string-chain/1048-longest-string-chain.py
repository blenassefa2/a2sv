class Solution:
    """ a function to check the difference b/n two words"""
    def wordDifference(self, longWord, shortWord):
        # catch edge case
        if len(longWord) - len(shortWord) !=  1:
            return 2
        # initialize variables
        stack = []
        i = 0
        j = 0
        
        while i < len(longWord) and j < len(shortWord):
            if longWord[i] == shortWord[j]:
                i += 1
                j += 1
            else:
                i += 1
            
            if i - j > 1:
               
                return 2
        return 1
        
        
    def recurse(self, index, words, save):
        if index >= len(words):
            return 0
        if index in save:
            return save[index]
        answer = 0
        for i in range(index+ 1 , len(words)):
            if self.wordDifference(words[i], words[index]) == 1:
                answer = max(answer, self.recurse(i, words, save))
        save[index] = answer + 1
        return answer + 1
    def longestStrChain(self, words: List[str]) -> int:
        """
        let  n  be length of the whole array and 
        let m be length of the maximum word
        
        Time Complexity = O(mn^2)
        Space Complexity = O(n + m)
        
        """
        #initialize variables
        save = defaultdict(int)
        maximum = 0
        
        words.sort(key = lambda x: len(x))
        
        
        for i in range(len(words)):
            maximum = max(maximum, self.recurse(i, words, save))
        return maximum