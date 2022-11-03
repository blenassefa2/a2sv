class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # initilize my variables
        store = Counter(words)
        totalLength = 0
        selfPali = ""
        # iterate through words looking for pair and counting
        for word in words:
            if word[::-1] == word:
                if store[word] >=2:
                    totalLength += 2
                    store[word] -= 2
                elif store[word] == 1 and not selfPali:

                    selfPali = word

                    totalLength += 1
            elif store[word] > 0 and store[word[::-1]] > 0:
                totalLength += 2
                store[word] -= 1
                store[word[::-1]] -= 1

        totalLength *= 2
        return totalLength
    