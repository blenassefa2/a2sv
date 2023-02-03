class Solution:

    def __init__(self, w: List[int]):
        self.array = w
        

    def pickIndex(self) -> int:
        return choices(range(0,len(self.array)),weights = self.array, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()