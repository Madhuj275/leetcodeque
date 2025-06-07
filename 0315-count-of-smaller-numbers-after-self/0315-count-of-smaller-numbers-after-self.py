
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, index):
        while index <= self.n:
            self.tree[index] += 1
            index += index & -index
    
    def query(self, index):
        curr = 0
        while index > 0:
            curr += self.tree[index]
            index -= index & -index
        return curr

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        tree = FenwickTree(20000)
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = tree.query(nums[i] + 10001 - 1)
            tree.update(nums[i] + 10001)
        return ans 