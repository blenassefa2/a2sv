class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        def recurse(width,height, index,dp):
            if width > shelfWidth:
                return inf
            if index >= len(books):
                return 0
            if (index, width) in dp:
                return dp[(index, width)]
            bookWidth,bookHeight = books[index]
            sameRow = max(0, bookHeight - height) + recurse(width + bookWidth, max(height, bookHeight), index + 1,dp)
            nextRow = bookHeight + recurse(bookWidth, bookHeight, index + 1, dp)
            dp[(index, width)] = min(sameRow,nextRow)
            
            return dp[(index, width)]
        return recurse(0,0,0,defaultdict(int))