# single digit numbers except 1 nad 7 are not happy numbers. Loop until the number has 1 digit then return.
happy_singles = [1, 7]
class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            if n in happy_singles: return True
            return False
        s = 0
        while n > 9:
            s += (n%10)**2
            n = n//10
        s += n ** 2
        return self.isHappy(s)
