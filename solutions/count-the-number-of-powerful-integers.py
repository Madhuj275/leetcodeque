# Problem: Count the Number of Powerful Integers
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def dp(x):
            digits = list(map(int, str(x)))
            n = len(digits)
            suf_len = len(s)
            suf_digits = list(map(int, s))
            seen = {}

            def f(i, tight, zero, path):
                if i == n:
                    if len(path) < suf_len:
                        return 0
                    if path[-suf_len:] == suf_digits:
                        return 1
                    return 0

                key = (i, tight, zero, tuple(path[-suf_len:]))
                if key in seen:
                    return seen[key]

                res = 0
                max_d = digits[i] if tight else 9

                for d in range(0, max_d + 1):
                    if d > limit:
                        continue
                    nt = tight and (d == max_d)
                    nz = zero and d == 0
                    if zero and d == 0:
                        res += f(i + 1, nt, nz, path)
                    else:
                        res += f(i + 1, nt, False, path + [d])

                seen[key] = res
                return res

            return f(0, True, True, [])

        return dp(finish) - dp(start - 1)
