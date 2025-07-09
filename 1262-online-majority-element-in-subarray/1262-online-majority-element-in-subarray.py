class MajorityChecker:

    def __init__(self, arr: List[int]):
        n = len(arr)
        self.arr = arr
        self.occ = [[] for _ in range(max(arr) + 1)]
        for i in range(n):
            self.occ[arr[i]].append(i)
            

    def query(self, left: int, right: int, threshold: int) -> int:
        for i in range(8):
            rand = random.randint(left, right)
            check = self.arr[rand]
            leftind = bisect.bisect_left(self.occ[check], left)
            rightind = bisect.bisect_right(self.occ[check], right)
            if rightind - leftind >= threshold:
                return check
        return -1
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)