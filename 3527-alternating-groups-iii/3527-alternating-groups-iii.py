from sortedcontainers import SortedList
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:

        n = len(colors)
        colors+=colors
        prev = -1
        left = 0
        segments = SortedList()
        for i, x in enumerate(colors):
            if prev == -1:
                prev = x
                continue

            if x == prev:
                segments.add((left, i))
                left = i
            prev = x

        segments.add((left, len(colors)))

        cnt = Counter()
        for x, y in segments:
            if y <= n:
                cnt[y-x] += 1

        def bsearch(idx):
            l = 0
            r = len(segments)-1
            while l <= r:
                mid = (l+r)//2
                x, y = segments[mid]
                if x <= idx < y:
                    return mid
                if idx < x:
                    r = mid-1
                else:
                    l = mid+1

            return 0

        def update(idx):
            i = bsearch(idx)
            x, y = segments[i]
            
            newsegs = []
            remove = []
            # in middle
            if x < idx < y-1:
                newsegs.append((x, idx))
                newsegs.append((idx, idx+1))
                newsegs.append((idx+1, y))
                remove.append((x, y))
            # on an edge
            else:
                remove.append((x, y))
                # inside a segment of length one
                if idx == x and idx == y-1:
                    left = x
                    right = y
                    if i-1 >= 0:
                        prevx, prevy = segments[i-1]
                        left = prevx
                        remove.append((prevx, prevy))
                    if i+1 < len(segments):
                        nxtx, nxty = segments[i+1]
                        right = nxty
                        remove.append((nxtx, nxty))
                    newsegs.append((left, right))
                # on left edge
                elif idx == x:
                    if i-1 >= 0:
                        prevx, prevy = segments[i-1]
                        remove.append((prevx, prevy))
                        newsegs.append((prevx, prevy+1))
                    else:
                        newsegs.append((0, 1))
                    newsegs.append((x+1, y))
                # on right edge
                else:
                    if i+1 < len(segments):
                        nxtx, nxty = segments[i+1]
                        remove.append((nxtx, nxty))
                        newsegs.append((nxtx-1, nxty))
                    else:
                        newsegs.append((len(colors)-1, len(colors)))
                    newsegs.append((x, y-1))
            # update count and segments
            for seg in remove:
                segments.remove(seg)
                if seg[1] <= n:
                    cnt[seg[1]-seg[0]] -= 1

            for seg in newsegs:
                if seg[0] == seg[1]:
                    continue
                segments.add(seg)
                if seg[1] <= n:
                    cnt[seg[1]-seg[0]] += 1

        res = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                ans = 0
                todel = []
                for length, amt in cnt.items():
                    # no more, delete from dict
                    if amt == 0:
                        todel.append(length)
                    if length >= x:
                        ans += (length-x+1)*amt
                for length in todel:
                    del cnt[length]
                # find segment that goes over n
                edgeidx = bsearch(n)
                left, right = segments[edgeidx]
                length = right-left

                ans += max(0, min(length-x+1, n-left))
                res.append(ans)
            else:
                # didn't change
                if q[2] == colors[q[1]]:
                    continue
                colors[q[1]] = q[2]
                idx1 = q[1]
                idx2 = n+idx1
                # update index and rotated index
                update(idx1)
                update(idx2)
                
        return res