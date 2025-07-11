class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
        
    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += self.lowbit(i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res
    
    def lowbit(self, i):
        return i & (- i)
    
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        tree = BIT(n)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                dp[i] = 1
                tree.update(i + 1, 1)
        res = []
        for a, i, j in queries:
            if a == 2:
                if i > 1:
                    if dp[i - 1] == 1:
                        if nums[i - 1] <= j:
                            dp[i - 1] = 0
                            tree.update(i, -1)
                    else:
                        if nums[i - 1] > nums[i - 2] and nums[i - 1] > j:
                            dp[i - 1] = 1
                            tree.update(i, 1)
                if i < n - 2:
                    if dp[i + 1] == 1:
                        if nums[i + 1] <= j:
                            dp[i + 1] = 0
                            tree.update(i + 2, -1)
                    else:
                        if nums[i + 1] > nums[i + 2] and nums[i + 1] > j:
                            dp[i + 1] = 1
                            tree.update(i + 2, 1)
                if i > 0 and i < n - 1:
                    if dp[i] == 1:
                        if j <= nums[i - 1] or j <= nums[i + 1]:
                            dp[i] = 0
                            tree.update(i + 1, -1)
                    else:
                        if j > nums[i - 1] and j > nums[i + 1]:
                            dp[i] = 1
                            tree.update(i + 1, 1)
                nums[i] = j
            else:
                if j - i < 2:
                    res.append(0)
                elif i + 1 == j:
                    if nums[i + 1] > nums[i] and nums[i + 1] > nums[i + 1]:
                        res.append(1)
                    else:
                        res.append(0)
                else:
                    res.append(tree.query(j) - tree.query(i + 1))
               
        return res