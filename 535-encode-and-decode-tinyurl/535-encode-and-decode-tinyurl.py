class Codec:
    def __init__(self):
        self.mapp = defaultdict()
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.mapp:
           
            n = 0
            stack = ""
            while n < len(longUrl):
                if longUrl[n] == "/":
                    stack = ""
                else:
                    stack = stack + longUrl
                n+=1
            self.mapp[longUrl] = "http://" + stack
        return self.mapp[longUrl]
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for i in self.mapp:
            if self.mapp[i] == shortUrl:
                return i
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))