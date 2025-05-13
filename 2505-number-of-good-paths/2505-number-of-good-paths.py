class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = 0
        n = len(vals)
        f = list(range(n))
        dct = defaultdict(list)
        mp = [[] for _ in range(n)]

        def find(u):
            if f[u] == u:
                return u

            f[u] = find(f[u])
            return f[u]

        def merge(u, v):
            fu, fv = find(u), find(v)
            if fu != fv:
                f[fu] = fv

        for i, val in enumerate(vals):
            dct[val].append(i)

        for u, v in edges:
            uVal, vVal = vals[u], vals[v]
            if uVal >= vVal:
                mp[u].append(v)
            else:
                mp[v].append(u)

        keys = sorted(dct.keys())
        for key in keys:
            arr = dct[key]
            for u in arr:
                for v in mp[u]:
                    merge(u, v)

            groups = defaultdict(list)
            for u in arr:
                groups[find(u)].append(u)

            for root, nodes in groups.items():
                ln = len(nodes)
                ans += ln*(ln+1)>>1

        return ans