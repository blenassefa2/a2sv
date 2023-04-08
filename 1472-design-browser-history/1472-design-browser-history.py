class Page:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.nxt = nxt
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        self.current.nxt = Page(url, None, self.current)
        self.current = self.current.nxt

    def back(self, steps: int) -> str:
        
        
        while self.current.prev:
            if steps == 0:
                break
            self.current = self.current.prev
            steps -= 1
        return self.current.value

    def forward(self, steps: int) -> str:
        while self.current.nxt:
            if steps == 0:
                break
            self.current = self.current.nxt
            steps -= 1
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)