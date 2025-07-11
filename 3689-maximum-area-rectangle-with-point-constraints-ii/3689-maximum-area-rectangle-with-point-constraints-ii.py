class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        xs = list(sorted(set(xCoord)))
        x2i = {}
        for i, x in enumerate(xs):
            x2i[x] = i
        n = len(xs)
        st = ST(n)

        y2xs = {}
        for x, y in zip(xCoord, yCoord):
            y2xs.setdefault(y, []).append(x)

        res = 0
        # prev_y on x
        prev_y = {x: float('-inf') for x in xCoord}
        for y2 in sorted(y2xs.keys()):
            xs = list(sorted(y2xs[y2]))
            for x1, x2 in zip(xs, xs[1:]):
                y11 = prev_y[x1]
                y12 = prev_y[x2]
                if y11 == y12 and y11 != float('-inf'):
                    y1 = y11
                    # rect detected
                    i1, i2 = x2i[x1], x2i[x2]
                    if st.query(1, 0, n-1, i1+1, i2-1) < y1:
                        res = max(res, (x2 - x1) * (y2 - y1))
            # update st
            for x in xs:
                st.update(1, 0, n-1, x2i[x], y2)
                prev_y[x] = max(prev_y[x], y2)
        return res if res > 0 else -1

class ST:
    def __init__(self, n):
        self.t = [-1] * 4*n

    def query(self, s, sl, sr, l, r):
        if l > r:
            return float('-inf')
        if l == sl and r == sr:
            return self.t[s]
        sm = (sl + sr) // 2
        return max(self.query(s*2, sl, sm, l, min(r, sm)), self.query(s*2+1, sm+1, sr, max(l, sm+1), r))

    # update(1, 0, n-1, p, val)
    def update(self, s, sl, sr, pos, new_val):
        if sl == sr:
            self.t[s] = new_val
        else:
            sm = (sl + sr) // 2
            if pos <= sm:
                self.update(s*2, sl, sm, pos, new_val)
            else:
                self.update(s*2+1, sm+1, sr, pos, new_val)

            self.t[s] = max(self.t[s*2], self.t[s*2 + 1])


