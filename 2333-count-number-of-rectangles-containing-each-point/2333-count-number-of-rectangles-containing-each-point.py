class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for l, h in rectangles: mp[h].append(l)
        for v in mp.values(): v.sort()
        ans = []
        for x, y in points: 
            cnt = 0 
            for yy in range(y, 101): 
                if yy in mp: cnt += len(mp[yy]) - bisect_left(mp[yy], x)
            ans.append(cnt)
        return ans 