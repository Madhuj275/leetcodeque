class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []
        for m in meetings:
            if not merged or m[0] > merged[-1][1]:
                merged.append(m)
            else:
                merged[-1][1]=max(merged[-1][1],m[1])
        tc=0
        for s,e in merged:
            tc+=e-s+1
        return days-tc








        