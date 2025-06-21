class DinnerPlates:

    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity
        self.nonFullSt = [] # min heap of non-full stacks

    def push(self, val: int) -> None:
        while self.nonFullSt:
            stID = heappop(self.nonFullSt)
            if stID < len(self.arr) and len(self.arr[stID]) < self.capacity:
                # This check is needed because the nonFullSt Id can be greater than self.arr size in case we poped many empy stacks from self.arr in a pop(self) function
                self.arr[stID].append(val)
                if len(self.arr[stID]) == self.capacity:
                    heappush(self.nonFullSt, stID)
                return
        if self.arr:
            if len(self.arr[-1]) == self.capacity:
                self.arr.append([val])
            else:
                self.arr[-1].append(val)
        else:
            self.arr.append([val])


    def pop(self) -> int:
        while self.arr:
            if len(self.arr[-1]) > 0:
                return self.arr[-1].pop()
            else:
                self.arr.pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if len(self.arr) > index and len(self.arr[index]) > 0:
            # this stack was full, add it to the nonFullSt heap
            if len(self.arr[index]) == self.capacity:
                heappush(self.nonFullSt, index)
            return self.arr[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)