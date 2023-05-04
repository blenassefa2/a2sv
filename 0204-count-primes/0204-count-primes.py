class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of eratosthenes 
        if n <3:
            return 0
        prime = [True]*(n+1)
        prime[0] = prime[1] = False
        i = 2
        while i*i < n:
            if prime[i]:
                j = i*i
                while j < n:
                    prime[j] = False
                    j += i
            i += 1

        return sum(prime) -1