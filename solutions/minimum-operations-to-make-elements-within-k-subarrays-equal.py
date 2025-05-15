# Problem: Minimum Operations to Make Elements Within K Subarrays Equal
# Difficulty: Unknown
# Solution:

from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        ln = len(nums)
        dp = [[math.inf for _ in range(k + 1)] for _ in range(ln + 1)]
        for i in range(len(dp)):
            dp[i][0] = 0
        
        def helper():
            if len(self.left) > len(self.right):
                num = self.left[-1]
            else:
                num = self.right[0]
            m, n = len(self.left), len(self.right)
            return abs((num * m) - (self.sumLeft) + (self.sumRight) - (num * n))
        
        def handle():
            if len(self.left) > len(self.right) + 1:
                last = self.left[-1]
                self.left.remove(last)
                self.right.add(last)
                self.sumLeft -= last
                self.sumRight += last
            if len(self.right) > len(self.left) + 1:
                last = self.right[0]
                self.right.remove(last)
                self.left.add(last)
                self.sumLeft += last
                self.sumRight -= last

        
        def remove(num):
            if num <= self.left[-1]:
                self.left.remove(num)
                self.sumLeft -= num
            else:
                self.right.remove(num)
                self.sumRight -= num
            handle()
            return
        
        def add(num):
            if (self.left and num <= self.left[-1]) or (self.right and num < self.right[0]) or (len(self.left) == 0 and len(self.right) == 0):
                self.left.add(num)
                self.sumLeft += num
            else:
                self.right.add(num)
                self.sumRight += num
            handle()
            return


        ele = nums[-x + 1:] if x != 1 else []
        ele.sort()
        mid = len(ele) // 2
        self.left = SortedList(ele[:mid + 1])
        self.right = SortedList(ele[mid + 1:])
        self.sumLeft = sum(self.left)
        self.sumRight = sum(self.right)
        for i in range(ln - x, -1, -1):
            add(nums[i])
            if i + x < ln:
                remove(nums[i + x])
            val = helper()
            for j in range(1, k + 1):
                dp[i][j] = min(val + dp[i + x][j - 1], dp[i + 1][j])
        return dp[0][k]
        