# Problem: Count the Number of Powerful Integers
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count(n):
            digits = list(map(int, str(n)))
            L = len(digits)
            suf_len = len(s)
            suf = [int(x) for x in s]
            dp = {}

            def dfs(i, tight, started, last_digits):
                if i == L:
                    if not started:
                        return 0
                    if len(last_digits) < suf_len:
                        return 0
                    if last_digits[-suf_len:] == suf:
                        return 1
                    return 0

                key = (i, tight, started, tuple(last_digits[-suf_len:]))
                if key in dp:
                    return dp[key]

                res = 0
                max_d = digits[i] if tight else 9

                for d in range(0, max_d + 1):
                    if d > limit:
                        continue
                    new_tight = tight and (d == max_d)
                    new_started = started or d != 0
                    new_last_digits = last_digits.copy()
                    if new_started:
                        new_last_digits.append(d)
                    res += dfs(i + 1, new_tight, new_started, new_last_digits)

                dp[key] = res
                return res

            return dfs(0, True, False, [])

        return count(finish) - count(start - 1)
