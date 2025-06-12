import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indexMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        new = (val not in self.indexMap or not self.indexMap[val])
        self.nums.append(val)
        #Record index
        self.indexMap[val].add(len(self.nums) - 1)
        return new

    def remove(self, val: int) -> bool:
        if val not in self.indexMap or not               self.indexMap[val]:
            return False
        removeIdx = self.indexMap[val].pop()
        lastIdx = len(self.nums) - 1
        lastVal = self.nums[lastIdx]

        if removeIdx != lastIdx:
            #lastVal into removeIdx
            self.nums[removeIdx] = lastVal
            #Update indexMap for lastVal
            self.indexMap[lastVal].remove(lastIdx)
            self.indexMap[lastVal].add(removeIdx)
        
        self.nums.pop()#pop last nums elem
        if not self.indexMap[val]: #remove key
            del self.indexMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()