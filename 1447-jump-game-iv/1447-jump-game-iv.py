class Solution:
    def minJumps(self, arr: List[int]) -> int:
        h={}
        for i,e in enumerate(arr):
            if e not in h:
                h[e] = []
            h[e].append(i)
        q = [(0,0)]
        while q:
            n,d = q.pop(0)
            if n == len(arr)-1:
                return d
            if n+1 == len(arr)-1:
                return d+1
            if n+1 < len(arr) and h.get(arr[n+1]):
                q.append((n+1,d+1))
            if n-1 >= 0 and h.get(arr[n-1]):
                q.append((n-1,d+1))
            for i in h[arr[n]]:
                if i != n:
                    q.append((i,d+1))
                if i == len(arr)-1:
                    return d+1
            h[arr[n]] = []