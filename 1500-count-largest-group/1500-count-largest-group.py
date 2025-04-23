class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = {}

        for i in range(1, n + 1):
            x = i
            dsum = 0
            while x > 0:
                dsum += x % 10
                x = x // 10

            if dsum not in count:
                count[dsum] = []
            count[dsum].append(i)
        
        max_len = max(len(val) for val in count.values())
        res = {k: val for k, val in count.items() if len(val) == max_len}

        return len(res)