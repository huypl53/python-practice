class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for mul in range(i*i, n, i):
                    primes[mul] = 0
        return sum(primes)

