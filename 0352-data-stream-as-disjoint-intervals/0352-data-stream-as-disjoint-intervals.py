class SummaryRanges:

    def __init__(self):
        self.seen = [False] * 10001

    def addNum(self, value: int) -> None:
        self.seen[value] = True

    def getIntervals(self) -> list[list[int]]:
        intervals = []
        idx = 0
        n = len(self.seen)
        while idx < n:
            if not self.seen[idx]:
                idx += 1
                continue
            #new interval
            start = idx
            while idx + 1 < n and self.seen[idx + 1]:
                idx += 1
            end = idx
            intervals.append([start, end])
            idx += 1
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()