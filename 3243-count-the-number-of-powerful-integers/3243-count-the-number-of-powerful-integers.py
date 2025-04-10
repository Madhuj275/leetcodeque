class Solution:
    def numberOfPowerfulInt(self, start: int, end: int, lim: int, suf: str) -> int:
        def count(num: str, suf: str, lim: int) -> int:
            if len(num) < len(suf):
                return 0
            if len(num) == len(suf):
                return 1 if num >= suf else 0

            res = 0
            pre_len = len(num) - len(suf)

            for i in range(pre_len):
                d = int(num[i])
                if d > lim:
                    res += (lim + 1) ** (pre_len - i)
                    return res
                res += d * (lim + 1) ** (pre_len - i - 1)

            if num[-len(suf):] >= suf:
                res += 1

            return res

        a = str(start - 1)
        b = str(end)
        return count(b, suf, lim) - count(a, suf, lim)
