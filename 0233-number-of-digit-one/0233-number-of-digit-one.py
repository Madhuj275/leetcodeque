class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while i <= n:
            div = i * 10
            a=(n // div) * i
            count += a + min(max(n % div - i + 1, 0), i)
            i *= 10
        return count