class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1
    
    
    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for a, b in self.counts.keys():
            if abs(x - a) == abs(y - b) and x != a:
                if (x, b) in self.counts and (a, y) in self.counts:
                    ans += self.counts[(a, b)] * self.counts[(x, b)] * self.counts[(a, y)]
        return ans
            


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)