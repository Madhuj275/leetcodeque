# Problem: Count the Number of Powerful Integers
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfPowerfulInt(self, a: int, b: int, lim: int, s: str) -> int:
        def ok(x):
            x = str(x)
            if not x.endswith(s):
                return False
            for d in x:
                if int(d) > lim:
                    return False
            return True

        def cnt(x):
            s_x = str(x)
            n = len(s_x)
            dp = {}

            def go(i, tight, zero):
                k = (i, tight, zero)
                if k in dp:
                    return dp[k]
                if i == n:
                    return 0 if zero else 1
                res = 0
                up = int(s_x[i]) if tight else 9
                for d in range(0, up + 1):
                    if d > lim:
                        continue
                    nt = tight and (d == up)
                    nz = zero and (d == 0)
                    res += go(i + 1, nt, nz)
                dp[k] = res
                return res

            return go(0, True, True)

        ans = 0
        for x in range(a, b + 1):
            if ok(x):
                ans += 1
        return ans
