class Node:
    def __init__(self, l: int, r: int):
        self.l, self.r = l, r
        if l == r:
            self.minVal = self.sumVal = 0
        else:
            mid = (l + r) // 2
            self.left, self.right = Node(l, mid), Node(mid + 1, r)
            self.minVal = min(self.left.minVal, self.right.minVal)
            self.sumVal = self.left.sumVal + self.right.sumVal
    
    def getMin(self, l: int, r: int) -> int:
        if self.l > r or self.r < l: return int(1e10)
        elif l <= self.l and self.r <= r: return self.minVal
        else:
            return min(self.left.getMin(l, r), self.right.getMin(l, r))
    
    def getSum(self, l: int, r: int) -> int:
        if self.l > r or self.r < l: return 0
        elif l <= self.l and self.r <= r: return self.sumVal
        else:
            return self.left.getSum(l, r) + self.right.getSum(l, r)
    
    def update(self, idx: int, value: int) -> int:
        if self.l > idx or self.r < idx: return 
        elif idx == self.l == self.r: self.minVal = self.sumVal = value
        else:
            self.left.update(idx, value)
            self.right.update(idx, value)
            self.minVal = min(self.left.minVal, self.right.minVal)
            self.sumVal = self.left.sumVal + self.right.sumVal
    
class BookMyShow:

    def __init__(self, n: int, m: int):
        # it would be easier to track vacant seats instead of occupied ones.
        self.rows = [0] * n # occupied seats in a row
        self.maxCapacity = m # max capacity of a row
        self.minRow = 0 # min index of the row with available seats, useful to avoid filling seats.
        self.root = Node(0, n - 1) # seg tree

    def gather(self, k: int, maxRow: int) -> List[int]:
        # Binary search over range to find out which one has required available seats.
        # invariant a valid idx with required capacity will be in range [L, R]
        l, r = self.minRow, maxRow
        if self.root.getMin(l, r) > self.maxCapacity - k: return []
        while l < r:
            mid = l + (r - l) // 2
            # if we have a closer to start range that can suffice.
            if self.root.getMin(l, mid) <= self.maxCapacity - k:
                r = mid
            else:
                l = mid + 1
        ans = [r, self.rows[r]]
        self.rows[r] += k
        self.root.update(r, self.rows[r])
        return ans
        

    def scatter(self, k: int, maxRow: int) -> bool:
        # Binary search over the range to find the range required to allocate seats.
        l, r = self.minRow, maxRow
        # invariant a valid last idx will be in range [l, r]
        if self.maxCapacity * (maxRow - self.minRow + 1) - self.root.getSum(self.minRow, maxRow) < k: return False
        while l < r:
            mid = l + (r - l) // 2
            if self.maxCapacity * (mid - self.minRow + 1) - self.root.getSum(self.minRow, mid) >= k: r = mid
            else:
                l = mid + 1
        # all rows till r - 1 will be completely filled and will be useless, so update minRow.
        self.rows[r] += k - ((self.maxCapacity * (r - self.minRow) - self.root.getSum(self.minRow, r - 1)) if r - 1 >= self.minRow else 0)
        self.root.update(r, self.rows[r])
        self.minRow = r
        return True 


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)