class Solution:
    def fib(self, n: int) -> int:
        def dp(n,dict_):
            if n < 2:
                return n 

            if dict_[n]:
                return(dict_[n])

            dict_[n] = self.fib(n-1) +self.fib(n-2)
            return dict_[n]
        
        return dp(n,defaultdict(int))