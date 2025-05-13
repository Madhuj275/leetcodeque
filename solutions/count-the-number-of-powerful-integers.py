# Problem: Count the Number of Powerful Integers
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(x):
            sfx_len = len(s)
            sfx_int = int(s)
            res = 0

            def ok(n):
                return all(int(c) <= limit for c in str(n))

            for l in range(sfx_len, 20):  
                p = 10 ** sfx_len
                low = 10 ** (l - sfx_len - 1) if l - sfx_len > 0 else 0
                high = 10 ** (l - sfx_len)

                for pre in range(low, high):
                    n = int(str(pre) + s)
                    if n > x:
                        break
                    if ok(n):
                        res += 1
            return res

        return count(finish) - count(start - 1)
