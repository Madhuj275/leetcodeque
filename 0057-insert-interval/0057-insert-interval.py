class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        if not intervals:
            return [newInterval]
        for i in intervals:
            if i[1] >= newInterval[0]:
                res.append([i[0],max(i[1],newInterval[1])])
            else:
                res.append(i)
        res.append(newInterval)   
        res.sort()
        merged = []
        for interval in res:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


