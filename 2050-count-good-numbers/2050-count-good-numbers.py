class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        even = (n + 1) // 2
        odd = n // 2

        a = 5
        b = even
        res1 = 1
        while b > 0:
            if b % 2 == 1:
                res1 = (res1 * a) % MOD
            a = (a * a) % MOD
            b //= 2

        a = 4
        b = odd
        res2 = 1
        while b > 0:
            if b % 2 == 1:
                res2 = (res2 * a) % MOD
            a = (a * a) % MOD
            b //= 2

        return (res1 * res2) % MOD