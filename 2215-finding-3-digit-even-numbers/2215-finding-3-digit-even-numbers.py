class Solution:
    def findEvenNumbers(self, digits):
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        res = []
        for d1 in range(1, 10):
            if freq[d1] == 0:
                continue
            freq[d1] -= 1
            for d2 in range(0, 10):
                if freq[d2] == 0:
                    continue
                freq[d2] -= 1

                for d3 in (0, 2, 4, 6, 8):
                    if freq[d3] > 0:
                        res.append(d1 * 100 + d2 * 10 + d3)

                freq[d2] += 1  
            freq[d1] += 1      

        return res
