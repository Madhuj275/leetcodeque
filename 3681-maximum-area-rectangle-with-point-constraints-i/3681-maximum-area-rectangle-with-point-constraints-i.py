class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n, points_set, res = len(points), set(map(tuple, points)), -1
        def helper(x1, x2, y1, y2):
            for x, y in points:
                if (x,y) in [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]:
                    continue
                if x1 <= x <= x2 and y1 <= y <= y2:
                    return True
            return False
        for i in range(n):
            for j in range(i+1, n):
                (x1, y1), (x2, y2) = points[i], points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in points_set and (x2, y1) in points_set:
                        x1, x2 = min(x1,x2), max(x1,x2)
                        y1, y2 = min(y1,y2), max(y1,y2)
                        if not helper(x1,x2,y1,y2):
                            area = abs(x2-x1)*abs(y2-y1)
                            res = max(res, area)
        return res