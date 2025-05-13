# Problem: Find the Count of Good Integers
# Difficulty: Unknown
# Solution:

class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        from math import factorial

        seen = set()
        power = 10 ** ((n - 1) // 2)
        skip = n % 2

        for i in range(power, power * 10):
            s = str(i)
            rev = s[::-1]
            pal = s + rev[skip:]
            if int(pal) % k == 0:
                seen.add(''.join(sorted(pal)))

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        res = 0
        for s in seen:
            cnt = [0] * 10
            for ch in s:
                cnt[int(ch)] += 1

            total = (n - cnt[0]) * fact[n - 1]
            for c in cnt:
                if c > 1:
                    total //= fact[c]
            res += total

        return res