class BIT:
    def __init__(self,n):
        self.ans = [0]*(n+1)

    def query(self,i):
        res = 0
        while i > 0:
            res += self.ans[i]
            i -= i&-i
        return res

    def update(self,i,val):
        while i < len(self.ans):
            self.ans[i] += val
            i += i&-i

class Solution:
    def minInteger(self, num, k):
        n, dict1, res = len(num), defaultdict(deque), ""

        for i,x in enumerate(num):
            dict1[x].append(i)

        result = BIT(n)

        for i in range(n):
            result.update(i+1,1)

        for i in range(n):
            for v in "0123456789":
                if dict1[v]:
                    idx = dict1[v][0]
                    cnt = result.query(idx)
                    if cnt <= k:
                        dict1[v].popleft()
                        k -= cnt
                        res += v
                        result.update(idx+1,-1)
                        break

        return res